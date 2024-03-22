# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


def snawfall(snowflakes_count=20, y=500, x=100, length=100):

    """ Функция рисования снегопада, кол-во снежинок: snowflakes_count, высота: y, начало: x, ширина: length"""

    snowflakes = {}
    snowflake_size = {'min': 5, 'max': 20}

    # заполняем словарь с параметрами снежинок
    for i in range(snowflakes_count):
        snowflakes[i] = {'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
                         'x': sd.random_number(x, x+length),
                         'y': y,
                         'factor_a': sd.random_number(1, 10) / 10,
                         'factor_b': sd.random_number(1, 10) / 10,
                         'factor_c': sd.random_number(1, 120)
                         }

    while True:

        sd.start_drawing()

        for snowflake_num, snowflake_parameter in snowflakes.items():

            start_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
            sd.snowflake(center=start_point,
                         length=snowflake_parameter['length'],
                         color=sd.background_color,
                         factor_a=snowflake_parameter['factor_a'],
                         factor_b=snowflake_parameter['factor_b'],
                         factor_c=snowflake_parameter['factor_c'])

            snowflake_parameter['x'] += sd.random_number(0, 2)
            snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length']

            next_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
            sd.snowflake(center=next_point,
                         length=snowflake_parameter['length'],
                         color=sd.COLOR_WHITE,
                         factor_a=snowflake_parameter['factor_a'],
                         factor_b=snowflake_parameter['factor_b'],
                         factor_c=snowflake_parameter['factor_c'])

            if snowflake_parameter['y'] < 50:
                snowflake_parameter['y'] = y
                snowflake_parameter['length'] = sd.random_number(snowflake_size['min'], snowflake_size['max'])
                snowflake_parameter['x'] = sd.random_number(x, x+length)

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


if __name__ == '__main__':
    snawfall()
    sd.pause()



