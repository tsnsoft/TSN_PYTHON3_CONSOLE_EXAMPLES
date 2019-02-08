#!/usr/bin/env python3
# coding=utf-8

# Программа должна считывать двумерный массив 5x6 из файла input.txt;
# выполнять задание варианта (получить измененный массив); выводить исходные
# данные в файл output.txt
# Задание варианта: найти количество нулей во второй строке таблицы, заменить
# на это значение максимальный элемент второго столбца.


def read_file(filename):
    in_file = open(filename, 'r')  # открываем файл в режиме чтения
    array = []  # инициализируем массив
    for line in in_file:  # проходим по каждой строке в файле
        sub_array = []  # инициализиурем подмассив
        # Разбиваем строку через пробелы и записываем их в массив
        str_nums = line.split(' ')
        for sn in str_nums:  # перебираем полученные строковые значения
            # Добавляем их в подмассив, преобразовав их в int
            sub_array.append(int(sn))
        array.append(sub_array)  # добавляем подмассив в массив
    return array


def write_file(filename, array):
    out_file = open(filename, 'w')  # открываем файл в режиме записи
    for row in array:  # перебираем каждую строку массива
        for num in row:  # перебираем каждое значение строки
            out_file.write("%d " % num)  # записываем это значение
        out_file.write('\n')  # дописываем перевод на новую строку


def main():
    array = read_file('input.txt')  # получаем массив
    zeroes = 0  # переменная для хранения количества нулей
    max_value = array[1][0]  # переменная для макс значения второго столбца
    for row in array:  # перебираем каждую строку
        # Находим максимальное значение
        if row[1] > max_value:
            max_value = row[1]
    for num in array[1]:  # перебираем вторую строку
        # Находим количество нулей
        if num == 0:
            zeroes += 1
    # Изменяем макс элемент 2 столбца на количество нулей во 2 строке
    for num in array:
        if num[1] == max_value:
            num[1] = zeroes
    write_file('output.txt', array)


if __name__ == '__main__':
    main()
