import sys

import requests


class Map():
    def __init__(self, coords, scale):
        self.coords_x = coords[0]
        self.coords_y = coords[1]
        self.scale = scale
        self.map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.coords_x},{self.coords_y}&spn={self.scale},{self.scale}&l=map"
        self.response = requests.get(self.map_request)

    def display_map(self):
        if not self.response:
            print("Ошибка выполнения запроса:")
            print(self.map_request)
            print("Http статус:", self.response.status_code, "(", self.response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(self.response.content)

        return map_file

    def increase(self):
       pass
