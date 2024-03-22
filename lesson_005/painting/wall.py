# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)


def draw_wall(house_x=500, house_y=500, x_for_each_row=100, start_y=100):

    """ Функция рисования кирпичной стены размером wall_size_x и wall_size_y из точки x_for_each_row и start_y """

    # размер кирпича
    x = 50
    y = 25

    # полкирпича
    half_brick = x // 2

    # количество кирпичей в ряду
    brick_x_count = house_x // x

    # количество рядов всего
    brick_y_count = house_y // y

    # начальная точка по иксу

    start_x = x_for_each_row

    x_count = 0

    wall_left_bottom = sd.get_point(start_x, start_y)
    wall_right_top = sd.get_point(start_x + house_x, start_y + house_y)
    sd.rectangle(wall_left_bottom, wall_right_top, color=sd.COLOR_DARK_RED)

    for brick_y in range(brick_y_count):

        # проверяем количество кирпичей в ряду
        if brick_y % 2 == 0:
            x_count = brick_x_count
        else:
            x_count += 1

        for brick_x in range(x_count):

            if brick_y % 2 == 1:
                if brick_x == 0:
                    start_position = sd.get_point(start_x, start_y)
                    end_position = sd.get_point(start_x + half_brick, start_y + y)
                elif brick_x == x_count - 1:
                    start_position = sd.get_point(start_x - half_brick, start_y)
                    end_position = sd.get_point(start_x, start_y + y)
                else:
                    start_position = sd.get_point(start_x - half_brick, start_y)
                    end_position = sd.get_point(start_x - half_brick + x, start_y + y)
            else:
                start_position = sd.get_point(start_x, start_y)
                end_position = sd.get_point(start_x + x, start_y + y)

            sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_BLACK, width=2)
            start_x += x

        # возвращаем кирпич в начало ряда
        start_x = x_for_each_row

        # поднимаем ряд на один выше
        start_y += y


if __name__ == '__main__':
    draw_wall()
    sd.pause()
