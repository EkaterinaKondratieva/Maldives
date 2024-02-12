import os

import pygame
from map import *

map = Map((2.294526, 48.858244), 0.002)
map_file = map.display_map()
# Инициализируем pygame
pygame.init()

screen = pygame.display.set_mode((1000, 800))
screen.fill('white')
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (30, 250))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.K_PAGEUP:
            pass

pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
