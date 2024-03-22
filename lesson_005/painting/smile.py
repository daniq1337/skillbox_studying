# -*- coding: utf-8 -*-
import random
import simple_draw as sd


def draw_smile(smile_size_x=100, smile_x=100, smile_y=100):

    """ Функция рисования смайла размером smile_size_x в точке smile_x, smile_y."""

    # размер смайла
    smile_size_y = smile_size_x // 2

    # рисуем уши
    smile_left_ear = sd.get_point(smile_x, smile_y + smile_size_y // 2)
    smile_right_ear = sd.get_point(smile_x + smile_size_x, smile_y + smile_size_y // 2)
    sd.circle(smile_left_ear, radius=smile_size_x//25, width=0, color=sd.COLOR_YELLOW)
    sd.circle(smile_right_ear, radius=smile_size_x//25, width=0, color=sd.COLOR_YELLOW)

    # рисуем лицо
    smile_left_bottom = sd.get_point(smile_x, smile_y)
    smile_right_top = sd.get_point(smile_x + smile_size_x, smile_y + smile_size_y)
    sd.ellipse(smile_left_bottom, smile_right_top, color=sd.COLOR_YELLOW)

    # рисуем рот
    smile_mouth_start = sd.get_point(smile_x+smile_size_x//3, smile_y+smile_size_y//3)
    mouth = sd.get_vector(smile_mouth_start, angle=-10, length=smile_size_x//10)
    mouth.draw(color=sd.COLOR_RED, width=2)
    smile_mouth_end = mouth.end_point

    mouth = sd.get_vector(smile_mouth_end, angle=0, length=smile_size_x//10)
    mouth.draw(color=sd.COLOR_RED, width=2)
    smile_mouth_end = mouth.end_point

    mouth = sd.get_vector(smile_mouth_end, angle=10, length=smile_size_x//10)
    mouth.draw(color=sd.COLOR_RED, width=2)

    # рисуем глаза
    smile_left_eye = sd.get_point(smile_x+smile_size_x//3, smile_y+2*smile_size_y//3)
    smile_right_eye = sd.get_point(smile_x + smile_size_x - smile_size_x // 3, smile_y + 2 * smile_size_y // 3)
    sd.circle(smile_left_eye, radius=smile_size_x//20, color=sd.COLOR_WHITE, width=0)
    sd.circle(smile_right_eye, radius=smile_size_x//20, color=sd.COLOR_WHITE, width=0)

    sd.circle(smile_left_eye, radius=smile_size_x//50, color=sd.COLOR_BLACK, width=0)
    sd.circle(smile_right_eye, radius=smile_size_x//50, color=sd.COLOR_BLACK, width=0)

    # рисуем нос
    smile_nose = sd.get_point(smile_x+smile_size_x//2, smile_y+smile_size_y//2)
    sd.circle(smile_nose, color=sd.COLOR_ORANGE, radius=smile_size_x//30, width=0)


if __name__ == '__main__':
    draw_smile()
    sd.pause()