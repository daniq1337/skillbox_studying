# -*- coding: utf-8 -*-
from pprint import pprint

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

sd.resolution = (1200, 800)
snowflakes = {}


class Snowflake:
    size = {'min': 5, 'max': 20}

    def __init__(self):
        self.length = sd.random_number(Snowflake.size['min'], Snowflake.size['max'])
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = sd.randint(sd.resolution[1] - 100, sd.resolution[1])
        self.factor_a = sd.random_number(1, 10) / 10
        self.factor_b = sd.random_number(1, 10) / 10
        self.factor_c = sd.random_number(30, 70)

    def draw(self, color=sd.COLOR_WHITE):
        start_point = sd.get_point(x=self.x, y=self.y)
        sd.snowflake(center=start_point,
                     length=self.length,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def hide(self, color=sd.background_color):
        self.draw(color)

    def move(self):
        self.x += sd.random_number(-2, 2)
        self.y -= Snowflake.size['max'] + 1 - self.length


def run_snowfall(snowflakes_count=0):
    """Запуск снегопада."""
    if len(snowflakes) != snowflakes_count:
        snowflakes[len(snowflakes)] = Snowflake()

    for num, snowflake in snowflakes.items():
        snowflake.hide()
        snowflake.move()
        snowflake.draw()

        if snowflake.y < 0:
            snowflakes[num] = Snowflake()


while True:
    sd.start_drawing()

    run_snowfall(snowflakes_count=20)

    sd.sleep(0.05)
    sd.finish_drawing()

    if sd.user_want_exit():
        break
