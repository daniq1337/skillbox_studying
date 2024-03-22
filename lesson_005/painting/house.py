import simple_draw as sd

sd.resolution = (1200, 800)


def draw_house(x=300, y=50, house_x=600, house_y=300):
    """ Функция рисования дома из точек x и y, размером house_x, house_y """

    # размеры окна
    window_size_x = 200
    window_size_y = 100

    # рисуем окно
    window_left_bottom = sd.get_point(x+house_x//3, y+house_y//3)
    window_right_top = sd.get_point(x+house_x//3+window_size_x, y+house_y//3+window_size_y)

    sd.rectangle(window_left_bottom, window_right_top, sd.COLOR_WHITE, 0)
    sd.rectangle(window_left_bottom, window_right_top, sd.COLOR_BLACK, 2)

    half_window_x = x+house_x//3+window_size_x//2
    top_window_y = y+house_y//3+window_size_y
    bottom_window_y = y+house_y//3

    window_start_point = sd.get_point(half_window_x, top_window_y)
    window_end_point = sd.get_point(half_window_x, bottom_window_y)
    sd.line(window_start_point, window_end_point, sd.COLOR_BLACK, 4)

    # рисуем крышу
    roof_peaks_list = [
        sd.get_point(x - house_x // 10, y + house_y),
        sd.get_point(x + house_x + house_x // 10, y + house_y),
        sd.get_point(x + house_x // 2, y + house_y + house_y//2)
    ]
    sd.polygon(roof_peaks_list, sd.COLOR_DARK_ORANGE, 0)
    sd.polygon(roof_peaks_list, sd.COLOR_BLACK, 2)


if __name__ == '__main__':
    draw_house()
    sd.pause()
