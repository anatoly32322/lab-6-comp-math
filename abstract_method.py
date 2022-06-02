from abc import ABC, abstractmethod
from typing import Callable, List
from prettytable import PrettyTable
from function_class import Function


class ABSMethod(ABC):
    func: Function
    y0: float
    a: float
    b: float
    func_array: List[tuple]
    func_array_h2: List[tuple]
    h: float
    eps: float
    result_table: PrettyTable
    runge_ratio: List[float]

    def __init__(self, func, y0, a, b, h, eps=1e-9):
        self.func = func
        self.y0 = y0
        self.a = a
        self.b = b
        self.h = h
        self.eps = eps
        self.result_table = PrettyTable()
        self.runge_ratio = []

    def _fill_table(self):
        for idx, xy in enumerate(self.func_array):
            self.result_table.add_row([idx,
                                       f'{xy[0]:.3}',
                                       f'{self.func.canon_func(xy[0]):.3}',
                                       f'{xy[1]:.3}',
                                       f'{self.runge_ratio[idx]:.5}'])

    def _reformat_table(self):
        self.result_table.clear()
        self.result_table.field_names = ['Индекс', 'X', 'Y_canon', 'Y_method', 'Коэффициент Рунге']

    def _calc_runge_ratio(self, p):
        # print(len(self.func_array), len(self.func_array_h2))
        for idx in range(len(self.func_array)):
            self.runge_ratio.append((self.func_array[idx][1] - self.func_array_h2[2 * idx][1]) / (pow(2, p) - 1))

    def print_table(self):
        print(self.result_table)

    @abstractmethod
    def method(self, func, y0, a, b, h, eps):
        pass

    @abstractmethod
    def get_method(self):
        pass
