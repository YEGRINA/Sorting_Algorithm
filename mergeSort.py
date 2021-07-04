import time
import pygame
from colors import *

pygame.init()
sel = pygame.mixer.Sound('sound/button-37a.wav')
finish = pygame.mixer.Sound('sound/button-4.wav')


def merge(data, start, mid, end):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end + 1):
        if p > mid:
            tempArray.append(data[q])
            q += 1
        elif q > end:
            tempArray.append(data[p])
            p += 1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p += 1
        else:
            tempArray.append(data[q])
            q += 1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1


def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid + 1, end, drawData, timeTick)

        merge(data, start, mid, end)

        sel.play()
        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
        else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    finish.play()
    drawData(data, [PINK for x in range(len(data))])


def merge_explanation():
    text = '* Explanation *\n' \
           'Worst case: O(nlogn)\n' \
           'Average case: O(nlogn)\n' \
           'Best case: O(nlogn)\n' \

    return text
