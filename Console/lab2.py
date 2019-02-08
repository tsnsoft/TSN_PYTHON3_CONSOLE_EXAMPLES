#!/usr/bin/env python3
# coding=utf-8

# Программа получает значения A B X и выводит Y согласно
# y = (4 * a^2 + b * x) / (b - x), x > 4
# y = 3 * (a + b + x^2), x <= 4


def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x > 4:
        print("X больше 4, применяем формулу:")
        print("(4 * a^2 + b * x) / (b - x)")
        y = (4 * a ** 2 + b * x) / (b - x)
    else:
        print("X меньше или равно 4, применяем формулу:")
        print("3 * (a + b + x^2)")
        y = 3 * (a + b + x ** 2)
    print("y = %.1f" % y)


if __name__ == '__main__':
    main()
