from abstract_method import ABSMethod
from prettytable import PrettyTable


class Euler(ABSMethod):
    def __init__(self, func, y0, a, b, h, eps=1e-9):
        super().__init__(func, y0, a, b, h, eps)

    def get_method(self):
        return 'Метод Эйлера'

    def method(self, func, y0, a, b, h, eps):
        func_array = [(a, y0)]
        x = a + h
        while abs(x - b) > 1e-9:
            func_array.append((x, func_array[-1][1] + h * func(x, func_array[-1][1])))
            x += h
        return func_array

    def solve(self):
        self._reformat_table()
        self.func_array = self.method(self.func.y_func, self.y0, self.a, self.b, self.h, self.eps)
        self.func_array_h2 = self.method(self.func.y_func, self.y0, self.a, self.b, self.h / 2, self.eps)
        self._calc_runge_ratio(2)
        self._fill_table()
        self.print_table()
        return self.func_array
