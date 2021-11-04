import string
import random


LETTERS = string.ascii_lowercase


def make_zero():
     zero = [random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS),
            random.choice(LETTERS) + ' ' + ' ' + random.choice(LETTERS),
            random.choice(LETTERS) + ' ' + ' ' + random.choice(LETTERS),
            random.choice(LETTERS) + ' ' + ' ' + random.choice(LETTERS),
            random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS)]
     return zero


def make_one():
    one = [' ' + ' ' + ' ' + random.choice(LETTERS),
        ' ' + ' ' + ' ' + random.choice(LETTERS),
        ' ' + ' ' + ' ' + random.choice(LETTERS),
        ' ' + ' ' + ' ' + random.choice(LETTERS),
        ' ' + ' ' + ' ' + random.choice(LETTERS)]
    return one


def make_two():
    two = [random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS),
       ' ' + ' ' + ' ' + random.choice(LETTERS),
       random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS),
       random.choice(LETTERS) + ' ' + ' ' + ' ',
       random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS)]
    return two



def make_three():
    three = [random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS),
             ' ' + ' ' + ' ' + random.choice(LETTERS),
             random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS),
             ' ' + ' ' + ' ' + random.choice(LETTERS),
             random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS)]
    return three


def make_four():
    four = [random.choice(LETTERS) + ' ' + ' ' + random.choice(LETTERS),
            random.choice(LETTERS) + ' ' + ' ' + random.choice(LETTERS),
            random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS) + random.choice(LETTERS),
            ' ' + ' ' + ' ' + random.choice(LETTERS),
            ' ' + ' ' + ' ' + random.choice(LETTERS)]
    return four


def make_five():
    five = [random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
           random.choice(LETTERS)+' '+' '+' ',
           random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
           ' '+' '+' '+random.choice(LETTERS),
           random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)]
    return five

    
def make_six():
    six = [random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
           random.choice(LETTERS)+' '+' '+' ',
           random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
           random.choice(LETTERS)+' '+' '+random.choice(LETTERS),
           random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)]
    return six


def make_seven():
    seven = [random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
             ' '+' '+' '+random.choice(LETTERS),
             ' '+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
             ' '+' '+' '+random.choice(LETTERS),
             ' '+' '+' '+random.choice(LETTERS)]
    return seven


def make_eight():
    eight = [random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
             random.choice(LETTERS)+' '+' '+random.choice(LETTERS),
             random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
             random.choice(LETTERS)+' '+' '+random.choice(LETTERS),
             random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)]
    return eight


def make_nine():
    nine = [random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
            random.choice(LETTERS)+' '+' '+random.choice(LETTERS),
            random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS)+random.choice(LETTERS),
            ' '+' '+' '+random.choice(LETTERS),
            ' '+' '+' '+random.choice(LETTERS)]
    return nine






