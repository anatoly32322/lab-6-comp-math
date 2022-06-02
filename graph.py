import matplotlib.pyplot as plt
import numpy as np
from function_class import Function


def draw(points: [[tuple], [tuple]], function: Function):
    points_euler = points[0]
    points_adams = points[1]
    plt.grid(True, which='both')
    plt.xlabel('X')
    plt.ylabel('Y')

    min_x = min(points_euler, key=lambda q: q[0])[0]
    max_x = max(points_euler, key=lambda q: q[0])[0]
    x = np.linspace(min_x - 0.1, max_x + 0.1, len(points_euler))
    plt.plot(x, function.canon(x), "c", label=function.canon_str)

    for x, y in splitting_list(points_euler):
        plt.plot(x, y, "ro")

    for x, y in splitting_list(points_adams):
        plt.plot(x, y, "bo")

    plt.legend(loc="best", fontsize='x-small')
    plt.show()


def splitting_list(lst):
    for idx in lst:
        yield idx[0], idx[1]
