# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from painting.house import draw_house
from painting.wall import draw_wall
from painting.smile import draw_smile
from painting.rainbow import draw_rainbow
from painting.snowfall import snawfall
from painting.tree import draw_tree

sd.resolution = (1400, 800)

# размеры дома
house_x = 600
house_y = 300

# левый нижний угол дома
x = 400
y = 50

draw_wall(house_x=house_x, house_y=house_y, x_for_each_row=x, start_y=y)
draw_house(x=x, y=y, house_x=house_x, house_y=house_y)
draw_smile(smile_size_x=70, smile_x=x+house_x//2-80, smile_y=y+house_y//2)
draw_rainbow(500, -200, radius=1000, width=20)

root_point = sd.get_point(1200, 50)
draw_tree(point=root_point)

# рисуем солнце
sun_x = 200
sun_y = 600

sun_radius = 80
ray_length = 100

sun_position = sd.get_point(sun_x, sun_y)
sd.circle(sun_position, radius=sun_radius, width=0)


snawfall(y=400, x=0, length=200)

sd.pause()


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
