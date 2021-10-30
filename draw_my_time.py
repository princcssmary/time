import generate_num_for_draw
import time


FUNC_DICT = {'0': generate_num_for_draw.make_zero, '1': generate_num_for_draw.make_one,
             '2': generate_num_for_draw.make_two, '3': generate_num_for_draw.make_three,
             '4': generate_num_for_draw.make_four, '5': generate_num_for_draw.make_five,
             '6': generate_num_for_draw.make_six, '7': generate_num_for_draw.make_seven,
             '8': generate_num_for_draw.make_eight, '9': generate_num_for_draw.make_nine}


def draw_num(num):
    num_list = list(str(num))
    num =(FUNC_DICT[num_list[0]]()[0] + ' ' + FUNC_DICT[num_list[1]]()[0] + ' ' + FUNC_DICT[num_list[2]]()[0] + ' ' + FUNC_DICT[num_list[3]]()[0] + '\n' +
          FUNC_DICT[num_list[0]]()[1] + ' ' + FUNC_DICT[num_list[1]]()[1] + ' ' + FUNC_DICT[num_list[2]]()[1] + ' ' + FUNC_DICT[num_list[3]]()[1] + '\n' +
          FUNC_DICT[num_list[0]]()[2] + ' ' + FUNC_DICT[num_list[1]]()[2] + ' ' + FUNC_DICT[num_list[2]]()[2] + ' ' + FUNC_DICT[num_list[3]]()[2] + '\n' +
          FUNC_DICT[num_list[0]]()[3] + ' ' + FUNC_DICT[num_list[1]]()[3] + ' ' + FUNC_DICT[num_list[2]]()[3] + ' ' + FUNC_DICT[num_list[3]]()[3] + '\n' +
          FUNC_DICT[num_list[0]]()[4] + ' ' + FUNC_DICT[num_list[1]]()[4] + ' ' + FUNC_DICT[num_list[2]]()[4] + ' ' + FUNC_DICT[num_list[3]]()[4])
    return num


def localtime():
    time.sleep(1)
    a = draw_num(time.strftime('%H%M'))
    return a


while True:
    print(localtime())

