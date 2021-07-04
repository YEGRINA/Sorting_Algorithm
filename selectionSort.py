import time
import pygame
from colors import *

pygame.init()
sel = pygame.mixer.Sound('sound/button-37a.wav')
finish = pygame.mixer.Sound('sound/button-4.wav')


def selection_sort(data, drawData, timeTick):
    for size in reversed(range(len(data))):
        max_i = 0
        for i in range(1, 1 + size):
            if data[i] > data[max_i]:
                max_i = i
        data[max_i], data[size] = data[size], data[max_i]

        sel.play()
        drawData(data, [YELLOW if x == i or x == max_i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    finish.play()
    drawData(data, [PINK for x in range(len(data))])


def selection_explanation():
    text = '* Explanation *\n' \
           'Worst case: O(n^2)\n' \
           'Average case: O(n^2)\n' \
           'Best case: O(n^2)\n'

    return text