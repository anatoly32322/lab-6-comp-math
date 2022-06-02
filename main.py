import numpy as np
from euler import Euler
from function_class import Function
from adams import Adams
from graph import draw


functions = [
    Function('x^3*e^(x^3)/3',
             '3*x^2*y + x^2*e^(x^3)',
             lambda x: pow(x, 3) * np.exp(pow(x, 3)) / 3,
             lambda x, y: 3 * pow(x, 2) * y + pow(x, 2) * np.exp(pow(x, 3))),
    Function('x^4 - x^2 + 2*|x|^3',
             'x^3 + x + 3*y/x',
             lambda x: pow(x, 4) - pow(x, 2) + 2 * pow(np.abs(x), 3),
             lambda x, y: pow(x, 3) + x + 3 * y / x),
]

result_points = []

methods = [Euler,
           Adams]

def main():
    print('Введите номер функции f\'(x, y), для которой хотите решить задачу Коши:')
    for idx, f in enumerate(functions):
        print(f'{idx + 1}. {f.y_str}')
    func_number = int(input())
    func = functions[func_number - 1]
    a, b = map(float, input('Введите интервал дифференцирования(a, b): ').split())
    h = float(input('Введите шаг дифференцирования(h): '))
    eps = float(input('Введите точность дифференцирования(eps): '))
    for method in methods:
        solver = method(func, func.canon_func(a), a, b, h, eps)
        print(solver.get_method())
        result_points.append(solver.solve())
    draw(result_points, func)


if __name__ == '__main__':
    main()
