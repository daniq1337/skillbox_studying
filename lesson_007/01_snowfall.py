# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1200, 800)


class Snowflake:

    snowflake_size = {'min': 5, 'max': 20}

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.random_number(500, 700)
        self.length = sd.random_number(Snowflake.snowflake_size['min'], Snowflake.snowflake_size['max'])
        self.factor_a = sd.random_number(1, 10) / 10
        self.factor_b = sd.random_number(1, 10) / 10
        self.factor_c = sd.random_number(30, 60)
        self.color = sd.COLOR_WHITE

    def draw(self, color=sd.COLOR_WHITE):
        self.start_point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=self.start_point,
                     length=self.length,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def move(self):
        self.x += sd.random_number(0, 2)
        self.y -= Snowflake.snowflake_size['max'] + 1 - self.length

    def clear_previous_picture(self, color=sd.background_color):
        self.draw(color)

    def can_fall(self):
        return self.y > 0


# flake = Snowflake()
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count=1):
    """ Функция создания списка count разнообразных снежинок. По умолчанию count = 1."""
    flakes = []
    for i in range(count):
        flake = Snowflake()
        start_point = sd.get_point(x=flake.x, y=flake.y)
        flakes.append({'center': start_point,
                       'length': flake.length,
                       'color': flake.color,
                       'factor_a': flake.factor_a,
                       'factor_b': flake.factor_b,
                       'factor_c': flake.factor_c})
    return flakes


flakes = get_flakes(5)

# flakes = get_flakes(count=20)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# sd.pause()
