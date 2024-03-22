# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


def draw_tree(point=sd.get_point(100, 100), angle=90, length=100):

    """Рисует дерево с рандомным отклонением угла ветвей в пределах 40% от 30 градусов,
       и с рандомным отклонением длины ветвей в пределах 20% от коэффициента 0.75
    """

    # список цветов для дерева
    colors = {1: sd.COLOR_RED,
              2: sd.COLOR_ORANGE,
              3: sd.COLOR_YELLOW,
              4: sd.COLOR_DARK_GREEN,
              }

    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length)
    sd.line(start_point=point, end_point=vector.end_point, color=colors[sd.random_number(1, 4)], width=2)

    next_point = vector.end_point

    delta = 30
    delta_deviation = delta * 0.4
    delta = delta + sd.random_number(round(-delta_deviation), round(delta_deviation))

    length = length * 0.75
    length_deviation = round(length * 0.2)
    length = length + sd.random_number(0, length_deviation)

    next_angle = round(angle + delta)
    draw_tree(point=next_point, angle=round(next_angle), length=round(length))

    next_angle = round(angle - delta)
    draw_tree(point=next_point, angle=round(next_angle), length=round(length))


if __name__ == '__main__':
    root_point = sd.get_point(500, 15)
    draw_tree(point=root_point)
    sd.pause()


