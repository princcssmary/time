import generate_num_for_draw
import time
import string
import random


FUNC_DICT = {'0': generate_num_for_draw.make_zero, '1': generate_num_for_draw.make_one,
             '2': generate_num_for_draw.make_two, '3': generate_num_for_draw.make_three,
             '4': generate_num_for_draw.make_four, '5': generate_num_for_draw.make_five,
             '6': generate_num_for_draw.make_six, '7': generate_num_for_draw.make_seven,
             '8': generate_num_for_draw.make_eight, '9': generate_num_for_draw.make_nine}


def draw_num(num, size):
    num_list = list(str(num))
    space = ' ' * size
    num = ((''.join([i * size for i in FUNC_DICT[num_list[0]]()[0]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[1]]()[0]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[2]]()[0]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[3]]()[0]]) + '\n') * size +
           (''.join([i * size for i in FUNC_DICT[num_list[0]]()[1]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[1]]()[1]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[2]]()[1]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[3]]()[1]]) + '\n') * size +
           (''.join([i * size for i in FUNC_DICT[num_list[0]]()[2]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[1]]()[2]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[2]]()[2]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[3]]()[2]]) + '\n') * size +
           (''.join([i * size for i in FUNC_DICT[num_list[0]]()[3]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[1]]()[3]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[2]]()[3]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[3]]()[3]]) + '\n') * size +
           (''.join([i * size for i in FUNC_DICT[num_list[0]]()[4]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[1]]()[4]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[2]]()[4]]) + space + ''.join([i * size for i in FUNC_DICT[num_list[3]]()[4]]) + '\n') * size)
    return num


def localtime(size):
    time.sleep(1)
    a = draw_num(time.strftime('%H%M'), size)
    return a


if __name__ == '__main__':
    size = int(input('Введите размер: '))
    while True:
        print(localtime(size))

