import simple_draw as sd

sd.resolution = (1200, 800)


def draw_rainbow(rainbow_x=0, rainbow_y=0, radius=500, width=10):

    """ Функция отрисовки радуги с центром в точках -> rainbow_x и rainbow_y, радиусом -> radius,
    толщиной -> width."""

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

    step = 0

    for color in rainbow_colors:
        point = sd.get_point(rainbow_x, rainbow_y)
        sd.circle(center_position=point, radius=radius + step, color=color, width=width)
        step += width


if __name__ == '__main__':
    draw_rainbow()
    sd.pause()
