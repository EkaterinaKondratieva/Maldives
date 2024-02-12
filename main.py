import os

import pygame
from map import *

map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
response = requests.get(map_request)
map_file = display_map((0, 0), 0)
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
        pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
