import sys

import requests


class Map():
    def __init__(self, coords, scale):
        self.coords_x = coords[0]
        self.coords_y = coords[1]
        self.scale = scale

    def display_map(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.coords_x},{self.coords_y}&spn={self.scale},{self.scale}&l=map"
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

        return map_file

    def increase(self):
        if self.scale > 0.003:
            self.scale -= 0.003

    def reduce(self):
        if self.scale < 0.03:
            self.scale += 0.003

