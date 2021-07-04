import time
import pygame
from colors import *

pygame.init()
sel = pygame.mixer.Sound('sound/button-37a.wav')
finish = pygame.mixer.Sound('sound/button-4.wav')


def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                sel.play()
                drawData(data, [YELLOW if x == j or x == j + 1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)

    finish.play()
    drawData(data, [PINK for x in range(len(data))])


def bubble_explanation():
    text = '* Explanation *\n' \
           'Worst case: O(n^2)\n' \
           'Average case: O(n^2)\n' \
           'Best case: O(n^2)\n' \

    return text
