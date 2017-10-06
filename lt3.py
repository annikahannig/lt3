#!/usr/bin/env python3

import math

LEO = lambda x, y: \
      math.sqrt(x**2 + (0.1 + -1.2*y - abs(x)*((2.4-abs(x))/2))**2) < 0.9


def render(w, h, fn):
    return [["*" if fn(-1.0 + 2*x/w, -1.0+2*y/h) else " " for x in range(0, w)]
            for y in range(0, h)]


def view(res):
    for row in res:
        print("".join(row))


def main():
    view(render(50, 30, LEO))


if __name__ == '__main__':
    main()
