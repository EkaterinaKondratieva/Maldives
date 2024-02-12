import sys

import requests


def display_map(coords, scale):
    coords_x = 2.294526
    coords_y = 48.858244
    scale = 0.002
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords_x},{coords_y}&spn={scale},{scale}&l=map"
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