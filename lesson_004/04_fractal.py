# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(point, angle, length=100):

    """Рисует ствол из начальной точки и 2 ветви дерева"""

    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()

    next_point = vector.end_point
    delta = 30
    length *= .75

    next_angle = angle - delta
    draw_branches(point=next_point, angle=next_angle, length=length)

    next_angle = angle + delta
    draw_branches(point=next_point, angle=next_angle, length=length)


sd.resolution = (1200, 800)
point = sd.get_point(500, 15)


root_point = sd.get_point(700, 15)
draw_branches(point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_branches(point, angle, length=100):
    """Рисует дерево с рандомным отклонением угла ветвей в пределах 40% от 30 градусов,
       и с рандомным отклонением длины ветвей в пределах 20% от коэффициента 0.75
    """
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
    draw_branches(point=next_point, angle=round(next_angle), length=round(length))

    next_angle = round(angle - delta)
    draw_branches(point=next_point, angle=round(next_angle), length=round(length))


colors = {1: sd.COLOR_RED,
          2: sd.COLOR_ORANGE,
          3: sd.COLOR_YELLOW,
          4: sd.COLOR_DARK_GREEN,
          }

root_point = sd.get_point(300, 15)
draw_branches(point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.random_number()

sd.pause()


