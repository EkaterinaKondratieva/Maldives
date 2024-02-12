import os

import pygame
from map import *

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
screen.fill('white')

map = Map((2.294526, 48.858244), 0.011)
map_file = map.display_map()
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (30, 250))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                map.increase()
                map_file = map.display_map()
            if event.key == pygame.K_PAGEDOWN:
                map.reduce()
                map_file = map.display_map()
    screen.blit(pygame.image.load(map_file), (30, 250))
    pygame.display.flip()
    fpsClock.tick(fps)
