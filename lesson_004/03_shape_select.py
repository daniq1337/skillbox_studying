# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (600, 600)


def draw_figure(start_point, side_count, angle, length, color):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length)
        elif side == side_count - 1:
            sd.line(vector.end_point, start_point, color=color)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector.draw(color=color)


def draw_triangle(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 3
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_quadrate(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 4
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_pentagon(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 5
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


def draw_hexagon(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    side = 6
    draw_figure(start_point=start_point, side_count=side, angle=angle, length=length, color=color)


shapes = {1: 'triangle',
          2: 'quadrate',
          3: 'pentagon',
          4: 'hexagon'}

print('Возможные фигуры:')
for key, value in shapes.items():
    print(key, ':', value)

while True:
    shape_number = input('Укажите номер фигуры > ')
    if shape_number.isdigit():
        shape_number = int(shape_number)
        if shape_number == 1:
            point = sd.get_point(300, 300)
            draw_triangle(start_point=point, angle=0, length=100, color=sd.COLOR_YELLOW)
            break

        elif shape_number == 2:
            point = sd.get_point(300, 300)
            draw_quadrate(start_point=point, angle=0, length=100, color=sd.COLOR_YELLOW)
            break

        elif shape_number == 3:
            point = sd.get_point(300, 300)
            draw_pentagon(start_point=point, angle=0, length=100, color=sd.COLOR_YELLOW)
            break

        elif shape_number == 4:
            point = sd.get_point(300, 300)
            draw_hexagon(start_point=point, angle=0, length=100, color=sd.COLOR_YELLOW)
            break

        else:
            print('Ошибка!: Неверно указан номер фигуры.')
    else:
        print('Ошибка!: Указана буква.')

sd.pause()
