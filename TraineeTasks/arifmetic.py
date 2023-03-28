"""
3. Есть функция:
"""


def add_gold(value):
    if value > 400_000:
        raise RuntimeError('Cannot add so much:( Please mercy!')
    print(f'{value} of gold added:) I am breathtaking!')


"""
Невозможно начислить больше n золота за раз.
Напишите функцию add_some_gold(value), принимающую любое значение, вычислите приблежнное кол-во золота, 
к максимально возможному, и начислите требуемое количество золота используя функцию add_gold.
"""


def add_some_gold(value: int) -> str:
    need_gold = value
    func_works_gold = 1
    maximum_gold = 1
    diff_gold = 2
    count = 0
    i = 0
    flag = False

    while count != 1_000_000:
        try:
            add_gold(func_works_gold)
            maximum_gold = func_works_gold
            func_works_gold *= 2
        except RuntimeError:
            while not add_gold(round(maximum_gold)):
                try:
                    add_gold(round(maximum_gold) + round(maximum_gold / diff_gold))
                    maximum_gold += round(maximum_gold / diff_gold)
                except RuntimeError:
                    diff_gold += 1
                    if i == 100:
                        flag = True
                        break
                    i += 1
                    continue
        count += 1

        if flag:
            break

    print()
    print(f'К максимальному кол-ву золота, возможному к начислению, максимально приближено {maximum_gold} едениц золота.')

    while need_gold > 0:
        if maximum_gold > need_gold:
            add_gold(need_gold)
            break
        else:
            add_gold(maximum_gold)
            need_gold -= maximum_gold


if __name__ == '__main__':
    add_some_gold(1_000_000)
