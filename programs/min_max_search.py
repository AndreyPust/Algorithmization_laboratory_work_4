#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import random


def max_search(list_search):
    """
    Функция поиска максимального элемента в переданном ей списке.
    """
    max_element = list_search[0]
    for i in list_search:
        if max_element < i:
            max_element = i
    return max_element


def min_search(list_search):
    """
    Функция поиска минимального элемента в переданном ей списке.
    """
    min_element = list_search[0]
    for i in list_search:
        if i < min_element:
            min_element = i
    return min_element


if __name__ == '__main__':
    # Необходимо создать программу, которая создает данные для анализа скорости работы
    # линейного поиска в списке минимального элемента и максимального элемента.

    current_list = [random.randint(-100, 100) for i in range(100000)]

    # Для записи результатов используются два файла в той же директории, что и данный модуль.
    filename_min = 'min_results.txt'
    filename_max = 'max_results.txt'

    # Получим данные при поиске максимального элемента в списке.
    for number in range(0, 400):

        with open(filename_max, 'a') as file:
            time_search = timeit.timeit(lambda: max_search(current_list), number=10)
            file.write(str(time_search) + '\n')
        file.close()

        # Получим данные при поиске минимального элемента в списке.
        with open(filename_min, 'a') as file:
            time_search = timeit.timeit(lambda: min_search(current_list), number=10)
            file.write(str(time_search) + '\n')
        file.close()

        # Увеличим размер данного списка.
        for i in range(1, 1001):
            current_list.append(random.randint(-100, 100))
