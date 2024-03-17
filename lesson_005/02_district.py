# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as s1h1r1, room2 as s1h1r2
from district.central_street.house2 import room1 as s1h2r1, room2 as s1h2r2
from district.soviet_street.house1 import room1 as s2h1r1, room2 as s2h1r2
from district.soviet_street.house2 import room1 as s2h2r1, room2 as s2h2r2

my_list = []

my_list.extend(s1h1r1.folks)
my_list.extend(s1h1r2.folks)
my_list.extend(s1h2r1.folks)
my_list.extend(s1h2r2.folks)

my_list.extend(s2h1r1.folks)
my_list.extend(s2h1r2.folks)
my_list.extend(s2h2r1.folks)
my_list.extend(s2h2r2.folks)

print('На районе живут', ', '.join(my_list))




