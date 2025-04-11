import math


def count_hypotenuse(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    print('Hypotenuse is', hypotenuse)


def count_square(a, b):
    square = a * b / 2
    print('Square is', square)


count_hypotenuse(2, 5)
count_square(4, 6)
