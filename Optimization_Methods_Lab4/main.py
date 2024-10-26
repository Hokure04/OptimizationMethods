import sympy
from sympy import Symbol
import math


def get_method():
    while True:
        print('1. Метод градиентного спуска')
        print('2. Метод наибыстрейшего спуска')
        number = int(input('Выбериете номер метода, который хотите использовать: '))
        if number == 1:
            gradient_descent_method()
        elif number == 2:
            fastest_descent_method()


def calculate_h(x_10, x_20, df_dx1, df_dx2):
    h_symbol = Symbol("h")
    x_11 = x_10 - h_symbol * df_dx1
    x_21 = x_20 - h_symbol * df_dx2
    f_x = func(x_11, x_21)
    diff_div = sympy.diff(f_x, h_symbol)
    diff_diff_div = sympy.diff(diff_div, h_symbol)
    diff_diff_diff = sympy.diff(diff_diff_div, h_symbol)
    h_parts = diff_diff_div.args
    h = -float(h_parts[0]) / float(diff_diff_diff)
    return h


def func(x_1, x_2):
    return 3 * x_1 * x_2 - x_1 ** 2 * x_2 - x_1 * x_2 ** 2
    # return 2*x_1 + 4*x_2 - x_1**2 - 2*x_2**2
    # return x_1 ** 2 + x_2 ** 2 + 1.5 * x_1 * x_2


def diff_func(x_1, x_2):
    df_dx1 = 3 * x_2 - 2 * x_1 * x_2 - x_2 ** 2
    df_dx2 = 3 * x_1 - x_1 ** 2 - 2 * x_1 * x_2
    # df_dx1 = 2 - 2*x_1
    # df_dx2 = 4 - 4*x_2
    # df_dx1 = 2 * x_1 + 1.5 * x_2
    # df_dx2 = 2 * x_2 + 1.5 * x_1
    return df_dx1, df_dx2


def gradient_descent_method():
    e = 0.05
    lambda_val = 0.25
    x_1, x_2 = 2, 1
    df_dx1, df_dx2 = diff_func(x_1, x_2)
    print(f'Δf = ({df_dx1}; {df_dx2})')
    f_x0 = func(x_1, x_2)
    print(f'f(x) = {f_x0}')
    f_x = f_x0 + 2 * e
    while abs(f_x - f_x0) > e:
        f_x0 = f_x
        x_1 = x_1 + lambda_val * df_dx1
        x_2 = x_2 + lambda_val * df_dx2
        print(f'x = ({x_1}; {x_2})')
        df_dx1, df_dx2 = diff_func(x_1, x_2)
        print(f'Δf = ({df_dx1}; {df_dx2})')
        f_x = func(x_1, x_2)
        print(f'f(x) = {f_x}')
    print('Итог:')
    print(f'x* =({x_1}; {x_2})')
    print(f'fmax = {f_x}')


def fastest_descent_method():
    e = 0.05
    x_10, x_20 = 2, 1
    iteration = 0
    df_dx1, df_dx2 = diff_func(x_10, x_20)
    print(f'df/dx1 = {df_dx1}')
    print(f'df/dx2 = {df_dx2}')
    h = calculate_h(x_10, x_20, df_dx1, df_dx2)
    while math.sqrt(df_dx1 ** 2 + df_dx2 ** 2) > e:
        x_1new = x_10 - h * df_dx1
        x_2new = x_20 - h * df_dx2
        print(f'x_1 = {x_1new}')
        print(f'x_1 = {x_2new}')
        df_dx1, df_dx2 = diff_func(x_1new, x_2new)
        print(f'df/dx1 = {df_dx1}')
        print(f'df/dx2 = {df_dx2}')
        x_10 = x_1new
        x_20 = x_2new
        iteration += 1

get_method()