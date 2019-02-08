#!/usr/bin/env python3
# coding=utf-8

# Пример решения квадратного уравнения
import math  # Подключение математического модуля

try:  # Защищенный блок 1
    a = float(input("Введите A="))
    b = float(input("Введите B="))
    c = float(input("Введите C="))
    try:  # Защищенный блок 2
        d = b * b - 4 * a * c
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print('d = ', d)
        print('x1 = ', round(x1, 2))
        print("x2 = " + format(x2, "#.2f"))
    except:  # Обработчик ошибок для защищенного блока 1
        print("Нет решения!")
except:  # Обработчик ошибок для защищенного блока 2
    print("Неверные входные данные!")
input("Нажмите Enter для выхода")  # Задержка перед выходом из программы
