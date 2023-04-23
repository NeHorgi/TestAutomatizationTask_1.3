"""
3. Есть функция:
"""
from functools import wraps
from time import perf_counter
from typing import Any


def add_gold(value):
    if value > 400_000:
        raise RuntimeError('Cannot add so much:( Please mercy!')
    print(f'{value} of gold added:) I am breathtaking!')


"""
Невозможно начислить больше n золота за раз.
Напишите функцию add_some_gold(value), принимающую любое значение, вычислите приблежнное кол-во золота, 
к максимально возможному, и начислите требуемое количество золота используя функцию add_gold.
"""


def add_some_gold(value):
    need_gold = value #Необходимое кол-во голды
    working_gold = need_gold #Кол-во голды, при котором функция add_gold() не райзит ошыбку
    check_gold = working_gold / 2 #Параметр уточнения кол-ва голды, нужен для поиска максимальной для начисления голды

    while need_gold:
        try:
            add_gold(working_gold)
            need_gold -= working_gold
            break
        except RuntimeError:
            working_gold = working_gold / 2
            check_gold = working_gold / 2

    while need_gold >= 0:
        if need_gold <= working_gold:
            add_gold(need_gold)
            break
        try:
            add_gold(working_gold + check_gold)
            need_gold -= (working_gold + check_gold)
            working_gold += check_gold
            check_gold = working_gold / 2
        except RuntimeError:
            check_gold = check_gold / 2


if __name__ == '__main__':
    add_some_gold(1_000_000)
