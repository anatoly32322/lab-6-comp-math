from typing import Callable


class Function:
    canon_str: str
    y_str: str
    canon: Callable
    y_: Callable

    def __init__(self, canon_str, y_str, canon, y_):
        self.canon_str = canon_str
        self.y_str = y_str
        self.canon = canon
        self.y_ = y_

    def get_canon(self) -> str:
        return self.canon_str

    def get_y_(self) -> str:
        return self.y_str

    def canon_func(self, x):
        return self.canon(x)

    def y_func(self, x, y):
        return self.y_(x, y)

    def __str__(self):
        return f'canon function: {self.get_canon()}\n' \
               f'y_ function: {self.get_y_()}'
