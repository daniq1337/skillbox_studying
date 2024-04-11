# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('\u001b[32m', '{} поел'.format(self.name), '\u001b[0m')
            self.fullness += 10
            self.house.food -= 10
        else:
            print('\u001b[31m', '{} нет еды'.format(self.name), '\u001b[0m')

    def work(self):
        print('\u001b[35m', '{} сходил на работу'.format(self.name), '\u001b[0m')
        self.house.money += 50
        self.fullness -= 10

    def watch_mtv(self):
        print('\u001b[34m', '{} смотрел MTV целый день'.format(self.name), '\u001b[0m')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('\u001b[33m', '{} сходил в магазин за едой'.format(self.name), '\u001b[0m')
            self.house.money -= 50
            self.house.food += 50
        else:
            print('\u001b[31m', '{} деньги кончились!'.format(self.name), '\u001b[0m')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('\u001b[32m', '{} Вьехал в дом'.format(self.name), '\u001b[0m')

    def act(self):
        if self.fullness <= 0:
            print('\u001b[31m', '{} умер...'.format(self.name), '\u001b[0m')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money)


my_sweet_home = House()
citizen = Man(name='Человек')
citizen.go_to_the_house(house=my_sweet_home)

for day in range(1, 21):
    print('\u001b[33m', '================ день {} =================='.format(day), '\u001b[0m')
    citizen.act()
    print('\u001b[32m', '--- в конце дня ---', '\u001b[0m')
    print('\u001b[36m', citizen, '\u001b[0m')
    print('\u001b[31m', my_sweet_home, '\u001b[0m')

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
