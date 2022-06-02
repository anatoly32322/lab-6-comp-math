from abstract_method import ABSMethod


class Adams(ABSMethod):
    def __init__(self, func, y0, a, b, h, eps=1e-9):
        super().__init__(func, y0, a, b, h, eps)

    def get_method(self):
        return 'Метод Адамса'

    def method(self, func, y0, a, b, h, eps):
        func_array = [(a, y0)]
        fun_t = [func(a, y0)]
        n = int((b - a) / h) + 1

        for i in range(1, 4):
            x_prev = func_array[i - 1][0]
            y_prev = func_array[i - 1][1]
            r1 = h * func(x_prev, y_prev)
            r2 = h * func(x_prev + h / 2, y_prev + r1 / 2)
            r3 = h * func(x_prev + h / 2, y_prev + r2 / 2)
            r4 = h * func(x_prev + h, y_prev + r3)

            x_cur = x_prev + h
            y_cur = y_prev + (r1 + 2 * r2 + 2 * r3 + r4) / 6

            func_array.append((x_cur, y_cur))
            fun_t.append(func(x_cur, y_cur))

        for i in range(4, n):
            x_cur = func_array[i - 1][0] + h

            y_pred = func_array[i - 1][1] + h / 24 * (
                    55 * fun_t[i - 1] - 59 * fun_t[i - 2] + 37 * fun_t[i - 3] - 9 * fun_t[i - 4])

            fun_t.append(func(x_cur, y_pred))

            y_cor = func_array[i - 1][1] + h / 24 * (
                    9 * fun_t[i] + 19 * fun_t[i - 1] - 5 * fun_t[i - 2] + fun_t[i - 3])

            while eps < abs(y_cor - y_pred):
                y_pred = y_cor
                fun_t[i] = func(x_cur, y_pred)
                y_cor = func_array[i - 1][1] + h / 24 *\
                        (9 * fun_t[i] + 19 * fun_t[i - 1] - 5 * fun_t[i - 2] + fun_t[i - 3])

            func_array.append((x_cur, y_cor))
        return func_array

    def solve(self):
        self._reformat_table()
        self.func_array = self.method(self.func.y_func, self.y0, self.a, self.b, self.h, self.eps)
        self.func_array_h2 = self.method(self.func.y_func, self.y0, self.a, self.b, self.h / 2, self.eps)
        self._calc_runge_ratio(4)
        self._fill_table()
        self.print_table()
        return self.func_array
