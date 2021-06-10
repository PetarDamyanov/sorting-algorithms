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
display_width = 300
display_height = 300
block_width = 30
padding_height = 10  # distance between block and and window in height
padding_width = 0  # distance between block and and window in width
lenght_of_arr = (display_width - padding_width - padding_width) / block_width
rising = True  # change rising or falling of sorting
# ===========================================================================

# generate list
# ========================================================================
arr_block = list()
for i in range(int(lenght_of_arr)):
    top = random.randint(padding_height * 2, display_height - padding_height * 2)
    arr_block.append(pygame.Rect((i * block_width) + padding_width, top, block_width, display_height - padding_height - top))
# ========================================================================

pygame.init()
pygame.display.set_caption('Merge sort')
DISPLAY = pygame.display.set_mode((display_width, display_height))
FPS_CLOCK = pygame.time.Clock()


def merge(arr):
    if len(arr) > 1:
        R, L = arr[len(arr) // 2:], arr[:len(arr) // 2]

        merge(R)
        merge(L)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k][0], L[i][0] = L[i][0], arr[k][0]
                arr[k], L[i] = L[i], arr[k]
                i += 1
            else:
                arr[k][0], R[j][0] = R[j][0], arr[k][0]
                arr[k], R[j] = R[j], arr[k]
                j += 1
            k += 1

            DISPLAY.fill(display_color)
            for block in range(len(arr_block)):
                pygame.draw.rect(DISPLAY, block_color, arr_block[block])

            pygame.display.update()
            FPS_CLOCK.tick(30)

        while i < len(L):
            arr[k][0], L[i][0] = L[i][0], arr[k][0]
            arr[k], L[i] = L[i], arr[k]
            i, k = i + 1, k + 1
        while j < len(R):
            arr[k][0], R[j][0] = R[j][0], arr[k][0]
            arr[k], R[j] = R[j], arr[k]
            j, k = j + 1, k + 1

        DISPLAY.fill(display_color)
        for block in range(len(arr_block)):
            pygame.draw.rect(DISPLAY, block_color, arr_block[block])

        pygame.display.update()
        FPS_CLOCK.tick(30)

def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

# draw blocks in their first form
# ===========================================================================
        DISPLAY.fill(display_color)
        for block in range(len(arr_block)):
            pygame.draw.rect(DISPLAY, block_color, arr_block[block])

        pygame.display.update()
        FPS_CLOCK.tick(30)
# ===========================================================================

# soriting algorithm
# ====================================================================================
        merge(arr_block)
        print(arr_block)
        sys.exit()
# ====================================================================================
# keep in mind that the time is slower because of the drawing of blocks and clock tick of 30 miliseconds


if __name__ == '__main__':
    main()
