import time
import pygame
from colors import *

pygame.init()
sel = pygame.mixer.Sound('sound/button-37a.wav')
finish = pygame.mixer.Sound('sound/button-4.wav')


def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            x[lmark], x[rmark] = x[rmark], x[lmark]
            lmark += 1
            rmark -= 1
    x[pivot_idx], x[rmark] = x[rmark], x[pivot_idx]
    return rmark


def quick_sort(data, drawData, timeTick):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotFirst(x, first, last)
            _qsort(x, first, splitpoint - 1)
            _qsort(x, splitpoint + 1, last)

            sel.play()
            drawData(data, [YELLOW if x == first or x == last else PURPLE if x == splitpoint
            else BLUE for x in range(len(data))])
            time.sleep(timeTick)

    _qsort(data, 0, len(data) - 1)
    finish.play()
    drawData(data, [PINK for x in range(len(data))])


def quick_explanation():
    text = '* Explanation *\n' \
           'Worst case: O(n^2)\n' \
           'Average case: O(nlogn)\n' \
           'Best case: O(nlogn)\n' \

    return text
