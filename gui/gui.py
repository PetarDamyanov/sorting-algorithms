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
pygame.display.set_caption('GUI for sort')
DISPLAY = pygame.display.set_mode((display_width, display_height))
FPS_CLOCK = pygame.time.Clock()

def main():

    while True:

        DISPLAY.fill(display_color)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for block in range(int(lenght_of_arr)):
            pygame.draw.rect(DISPLAY, block_color, arr[block])

        pygame.display.update()
        FPS_CLOCK.tick(30)


if __name__ == '__main__':
    main()
