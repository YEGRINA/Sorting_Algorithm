import time
import pygame
from colors import *

pygame.init()
sel = pygame.mixer.Sound('sound/button-37a.wav')
finish = pygame.mixer.Sound('sound/button-4.wav')


def insertion_sort(data, drawData, timeTick):
    for size in range(1, len(data)):
        val = data[size]
        i = size
        while i > 0 and data[i - 1] > val:
            data[i] = data[i - 1]
            i -= 1
        data[i] = val

        sel.play()
        drawData(data, [YELLOW if x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    finish.play()
    drawData(data, [PINK for x in range(len(data))])


def insertion_explanation():
    text = '* Explanation *\n' \
           'Worst case: O(n^2)\n' \
           'Average case: O(n^2)\n' \
           'Best case: O(n)\n' \

    return text