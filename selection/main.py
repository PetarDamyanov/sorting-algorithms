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
display_width = 600
display_height = 300
block_width = 10
padding_height = 10  # distance between block and and window in height
padding_width = 10  # distance between block and and window in width
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
pygame.display.set_caption('Selection sort')
DISPLAY = pygame.display.set_mode((display_width, display_height))
FPS_CLOCK = pygame.time.Clock()

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
        for step in range(len(arr)):
            min_index = step

            for i in range(step + 1, len(arr)):
                if rising:
                    if arr[i][1] > arr[min_index][1]:
                        min_index = i
                else:
                    if arr[i][1] < arr[min_index][1]:
                        min_index = i

            arr[step][0], arr[min_index][0] = arr[min_index][0], arr[step][0]
            arr[step], arr[min_index] = arr[min_index], arr[step]

            DISPLAY.fill(display_color)
            for block in range(len(arr)):
                pygame.draw.rect(DISPLAY, block_color, arr[block])

            pygame.display.update()
            FPS_CLOCK.tick(30)

# ====================================================================================
# keep in mind that the time is slower because of the drawing of blocks and clock tick of 30 miliseconds


if __name__ == '__main__':
    main()
