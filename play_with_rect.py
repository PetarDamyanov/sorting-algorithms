import pygame
from pygame.locals import *
from random import randint as random

display_width = 600
block_width = 10
lenght_of_arr = (display_width - 20) / block_width
arr = list()


for i in range(int(lenght_of_arr)):
    top = random(20, 280)
    arr.append(pygame.Rect(((i + 1) * 10), top, block_width, 290 - top))

print(arr)
print("======================================================")
n = len(arr)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arr[j][1] > arr[j + 1][1]:
            arr[j][0], arr[j + 1][0] = arr[j + 1][0], arr[j][0]
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
