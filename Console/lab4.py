#!/usr/bin/env python3
# coding=utf-8

# Имеется массив в два столбца и 10 строк. Реализовать команду заполнить
# случайными числами, при которой заполняется первый столбец. Реализовать
# команду выполнить задание, при которой второй столбец заполняется значениями
# по формуле y(i) = (сумма(K нечетных до i) + произведение(K четных до i)) /
# (i! - sin(Ki)/cos(Ki))**(1/3)

# Импортируем функцию из предыдущей работы для печати массивов
# Можно импортировать отдельные функции из модулей
import math
from lab3 import print_array
from random import randint


# Функция для создания массива по заданию
# max_value=100 - аргумент со стандартным значением 100
def random_array(max_value=100):
    array = []
    for i in range(0, 10):
        array.append([randint(0, max_value), 0])
    return array


def main():
    array = random_array()
    print_array(array)
    while True:
        print()  # переход на новую строку
        # Командный интерфейс
        print("1. Обновить массив")
        print("2. Выполнить задание")
        print("3. Выход")
        key = input('Введите команду: ')
        if key == '1':  # приравниваем старый массив к новому
            array = random_array()
            print_array(array)
        elif key == '2':  # выполняем задание
            print()  # переход на новую строку
            # Перебираем массив используя цикл for, используется range, т.к.
            # так удобнее будет изменять значения второго столбца
            for i in range(0, 10):
                if i == 0:
                    answer = 0  # т.к. числитель равен нулю
                else:
                    # Вычисляем числитель
                    summa = 0
                    proiz = 1
                    for j in range(i):
                        if array[j][0] % 2 == 0:
                            proiz *= array[j][0]
                        else:
                            summa += array[j][0]
                    chisl = summa + proiz
                    # используем тангенс т.к. sinA/cosA = tanA
                    znam = math.factorial(i) - math.tan(array[i][0])
                    value = chisl / znam
                    # Try блок позволяет избежать ошибки при возведении
                    # отрицательного числа в дробную степень
                    try:
                        # 1.0 чтобы python использовал тип float
                        answer = value ** (1.0 / 3)
                    except ValueError:
                        print("В python нельзя  возвести %d" % value, end='')
                        print("в дробную степень. Число будет пропущено")
                        continue  # переход на следующую итерацию
                array[i][1] = answer  # меняем 0 на ответ
            print_array(array)
        elif key == '3':  # выходим
            exit(0)


if __name__ == '__main__':
    main()
