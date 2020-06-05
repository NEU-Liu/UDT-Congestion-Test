import codecs
import matplotlib.pyplot as plt
import numpy as np
from collections.abc import Iterable


def flatten(x):
    result = []
    for el in x:
        if isinstance(x, Iterable) and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


def readcolumn(filename):
    fd = codecs.open(filename, mode='r', encoding='utf-8')
    line = fd.readline()
    column = []
    i = 0	
    while line and i < 1500:
        i = i + 1
        line_split_list = line.split()
        list_element = line_split_list[0]
        column.append(list_element)
        line = fd.readline()
    fd.close()
    column = flatten(column)
    column = list(map(float, column))
    return column

def plot(*filenames):
    if len(filenames) == 0:
        return
    for filename in filenames:
        column = readcolumn(filename)
        plt.plot(column, linewidth=1)
    plt.title("Mbps Send Rate", fontsize=20)
    plt.xlabel("Second", fontsize=10)
    plt.ylabel("Mbps", fontsize=10)
    plt.tick_params(axis='both', labelsize=10)
    plt.savefig("./demo.png")
    plt.show()


if __name__ == '__main__':
    plot("file1.txt","file2.txt")

