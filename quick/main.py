import sys
import pygame
from pygame.locals import *
import random

# colors = (red, gree, blue)
# ==============================================
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
pink = (255, 192, 203)
# ==============================================

# change properties
# ===========================================================================
display_color = black
block_color = blue
display_width = 1000
display_height = 300
block_width = 5
padding_height = 10  # distance between block and and window in height
padding_width = 0  # distance between block and and window in width
lenght_of_arr = (display_width - padding_width - padding_width) / block_width
rising = True  # change rising or falling of sorting
# ===========================================================================

# generate list
# ========================================================================
arr = list()
for i in range(int(lenght_of_arr)):
    top = random.randint(padding_height * 2, display_height - padding_height * 2)
    arr.append(pygame.Rect((i * block_width) + padding_width, top, block_width, display_height - padding_height - top))
# ========================================================================

pygame.init()
pygame.display.set_caption('Quick sort')
DISPLAY = pygame.display.set_mode((display_width, display_height))
FPS_CLOCK = pygame.time.Clock()


def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index][1]

    while start < end:

        while start < len(array) and array[start][1] <= pivot:
            start += 1

        while array[end][1] > pivot:
            end -= 1

        if(start < end):
            array[start][0], array[end][0] = array[end][0], array[start][0]
            array[start], array[end] = array[end], array[start]
            DISPLAY.fill(display_color)
            for block in range(len(arr)):
                pygame.draw.rect(DISPLAY, block_color, arr[block])

            pygame.display.update()
            FPS_CLOCK.tick(30)

    array[end][0], array[pivot_index][0] = array[pivot_index][0], array[end][0]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    DISPLAY.fill(display_color)
    for block in range(len(arr)):
        pygame.draw.rect(DISPLAY, block_color, arr[block])

    pygame.display.update()
    FPS_CLOCK.tick(30)

    return end

def quick(start, end, array):

    if (start < end):

        p = partition(start, end, array)

        quick(start, p - 1, array)
        quick(p + 1, end, array)


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

# draw blocks in their first form
# ===========================================================================
        DISPLAY.fill(display_color)
        for block in range(len(arr)):
            pygame.draw.rect(DISPLAY, block_color, arr[block])

        pygame.display.update()
        FPS_CLOCK.tick(30)
# ===========================================================================

# soriting algorithm
# ====================================================================================
        quick(0, len(arr) - 1, arr)
# ====================================================================================
# keep in mind that the time is slower because of the drawing of blocks and clock tick of 30 miliseconds


if __name__ == '__main__':
    main()
