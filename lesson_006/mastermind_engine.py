import random

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


def check_number(user_number, generated_number):
    user_number = list(map(int, user_number))

    bulls_and_cows = {
        'bulls': 0,
        'cows': 0
    }

    new_user_number = []
    new_generated_number = []

    for index in range(len(user_number)):
        if user_number[index] == generated_number[index]:
            bulls_and_cows['bulls'] += 1
        else:
            new_user_number.append(user_number[index])
            new_generated_number.append(generated_number[index])

    for index in range(len(new_user_number)):
        if new_user_number[index] in new_generated_number:
            bulls_and_cows['cows'] += 1

    print('быки -', bulls_and_cows['bulls'], 'коровы -', bulls_and_cows['cows'])


def is_gameover(user_number):
    user_number = list(map(int, user_number))
    return user_number == _numbers


if __name__ == '__main__':
    generated_number = generate_number()
    user_number = input('Введите число: ')
    check_number(user_number, generated_number)