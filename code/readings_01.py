import sys
import numpy


def main():
    filename = sys.argv[1]
    data = numpy.loadtxt(filename)
    for row_mean in numpy.mean(data, axis=1):
        print(row_mean)
    return None
