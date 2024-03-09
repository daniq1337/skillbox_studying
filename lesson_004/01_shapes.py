# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def pentagon(point, angle=0, length=100):
    for i in range(5):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        vector.draw()
        point = vector.end_point
        angle -= 72


def triangle(point, angle=0, length=100):
    for i in range(3):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        vector.draw()
        point = vector.end_point
        angle -= 120


def hexagon(point, angle=0, length=100):
    for i in range(6):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        vector.draw()
        point = vector.end_point
        angle -= 60


def square(point, angle=0, length=100):
    for i in range(4):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        vector.draw()
        point = vector.end_point
        angle -= 90


x, y = 100, 700
point = sd.get_point(x, y)
point_1 = sd.get_point(x, y-500)
point_2 = sd.get_point(x+600, y)
point_3 = sd.get_point(x+600, y-400)
pentagon(point=point, angle=10, length=150)
triangle(point=point_1, angle=20, length=200)
hexagon(point=point_2, angle=0, length=150)
square(point=point_3, angle=0, length=200)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
