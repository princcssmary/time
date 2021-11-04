import string
import random

a = string.ascii_lowercase


def make_zero():
     zero = [random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a),
            random.choice(a) + ' ' + ' ' + random.choice(a),
            random.choice(a) + ' ' + ' ' + random.choice(a),
            random.choice(a) + ' ' + ' ' + random.choice(a),
            random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a)]
     return zero


def make_one():
    one = [' ' + ' ' + ' ' + random.choice(a),
        ' ' + ' ' + ' ' + random.choice(a),
        ' ' + ' ' + ' ' + random.choice(a),
        ' ' + ' ' + ' ' + random.choice(a),
        ' ' + ' ' + ' ' + random.choice(a)]
    return one


def make_two():
    two = [random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a),
       ' ' + ' ' + ' ' + random.choice(a),
       random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a),
       random.choice(a) + ' ' + ' ' + ' ',
       random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a)]
    return two


make_two()


def make_three():
    three = [random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a),
             ' ' + ' ' + ' ' + random.choice(a),
             random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a),
             ' ' + ' ' + ' ' + random.choice(a),
             random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a)]
    return three


def make_four():
    four = [random.choice(a) + ' ' + ' ' + random.choice(a),
            random.choice(a) + ' ' + ' ' + random.choice(a),
            random.choice(a) + random.choice(a) + random.choice(a) + random.choice(a),
            ' ' + ' ' + ' ' + random.choice(a),
            ' ' + ' ' + ' ' + random.choice(a)]
    return four


def make_five():
    five = [random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
           random.choice(a)+' '+' '+' ',
           random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
           ' '+' '+' '+random.choice(a),
           random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)]
    return five

    
def make_six():
    
    six = [random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
           random.choice(a)+' '+' '+' ',
           random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
           random.choice(a)+' '+' '+random.choice(a),
           random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)]
    return six


def make_seven():
    seven = [random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
             ' '+' '+' '+random.choice(a),
             ' '+random.choice(a)+random.choice(a)+random.choice(a),
             ' '+' '+' '+random.choice(a),
             ' '+' '+' '+random.choice(a)]
    return seven


def make_eight():
    eight = [random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
             random.choice(a)+' '+' '+random.choice(a),
             random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
             random.choice(a)+' '+' '+random.choice(a),
             random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)]
    return eight


def make_nine():
    nine = [random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
            random.choice(a)+' '+' '+random.choice(a),
            random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a),
            ' '+' '+' '+random.choice(a),
            ' '+' '+' '+random.choice(a)]
    return nine







