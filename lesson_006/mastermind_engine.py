import random
from random import randint

_numbers = []


def generate_number():

    """ Создаёт список из четырех неповторяющихся цифр, первая цифра отлична от нуля. Возвращает список."""

    # создаём список из 3 случайных неповторяющихся цифр от 0 до 9
    global _numbers
    _numbers = random.sample(range(0, 9), 3)

    # создаём список для первой цифры, не равной нулю и трём другим
    list_for_first_number = []
    for i in range(1, 10, 1):
        if i not in _numbers:
            list_for_first_number.append(i)
        else:
            continue

    _numbers.insert(0, random.choice(list_for_first_number))
    return _numbers


def check_number():
    pass


def is_gameover():
    pass


generate_number()