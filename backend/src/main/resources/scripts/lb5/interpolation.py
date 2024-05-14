from input_output import *
import sys


def interpolation():
    type = input_type()
    if type == "true":
        dots = interpolation_function()
    else:
        dots = interpolation_coordinates()


def interpolation_function():
    num_dots = input_num_dots()
    left_border, right_border = input_borders()
    quation = input_quation()
    print()


def interpolation_coordinates():
    print()
