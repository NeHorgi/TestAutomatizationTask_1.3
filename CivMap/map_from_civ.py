import random


def start():
    print(f'Введите границы карты (Целые числа, по одному)')
    a = int(input())
    b = int(input())
    CurrentMap = GenerateMapFromCiv(a, b)
    print(f'Выберите тип карты: 1 - Пангея, 2 - Острова, 3 - Континенты')
    c = input()
    if c == '1':
        CurrentMap.create_pangea()
    elif c == '2':
        CurrentMap.create_islands()
    elif c == '3':
        CurrentMap.create_continents()
    CurrentMap.show_map()


class GenerateMapFromCiv:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ground_percent = ['∎' for _ in range(round(self.x * self.y * 0.3))]
        self.map = [['~' for _ in range(self.x)] for _ in range(self.y)]

    def create_pangea(self):

        count_of_lands = len(self.ground_percent)

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if len(self.map) // 3 <= i <= len(self.map) - len(self.map) // 2.5:
                    if len(self.map[i]) // 3 <= j <= len(self.map[i]) // 1.5:
                        if not count_of_lands:
                            break
                        self.map[i][j] = self.ground_percent.pop(0)
                        count_of_lands -= 1

        while count_of_lands:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if len(self.map) // (len(self.map) // 2) <= i <= len(self.map) // 1.2:
                        if len(self.map) // (len(self.map) // 2) <= j <= len(self.map) // 1.2:
                            if not count_of_lands:
                                break
                            chance = random.randint(0, 2)
                            if not chance:
                                if self.map[i][j] != '∎':
                                    self.map[i][j] = self.ground_percent.pop(0)
                                    count_of_lands -= 1

        return self.map

    def create_islands(self):
        if self.x >= self.y:
            islands_in_row = len(self.ground_percent) // self.x
        else:
            islands_in_row = len(self.ground_percent) // self.y

        for i in range(len(self.map)):
            current_islands = islands_in_row
            for j in range(len(self.map[i])):
                chance = random.randint(0, 2)
                if current_islands:
                    if not chance:
                        self.map[i][j] = '∎'
                        current_islands -= 1
                        self.ground_percent.pop(0)
                    else:
                        pass

        if not self.ground_percent:
            return self.map
        else:
            while self.ground_percent:
                island = random.randint(0, len(self.map) - 1)
                tile = random.randint(0, len(self.map[0]) - 1)

                if self.map[island][tile] != '∎':
                    self.map[island][tile] = '∎'
                    self.ground_percent.pop(0)

        return self.map

    def create_continents(self):
        first_continent = []
        second_continent = []

        count_of_lands_first_continent = len(self.ground_percent) // 2
        count_of_lands_second_continent = len(self.ground_percent) - count_of_lands_first_continent

        a = self.x // 2
        b = self.x - a
        c = self.y

        for _ in range(c):
            row = []
            for j in range(a):
                row.append('~')
            first_continent.append(row)

        for i in range(len(first_continent)):
            for j in range(len(first_continent[i])):
                if (len(first_continent) // 3) <= i <= len(first_continent) - len(first_continent) // 2.5:
                    if len(first_continent[i]) // 3 <= j <= len(first_continent[i]) // 2:
                        if not count_of_lands_first_continent:
                            break
                        first_continent[i][j] = self.ground_percent.pop(0)
                        count_of_lands_first_continent -= 1

        while count_of_lands_first_continent:
            for i in range(len(first_continent)):
                for j in range(len(first_continent[i])):
                    chance = random.randint(0, 2)
                    if not count_of_lands_first_continent:
                        break
                    if not chance:
                        first_continent[i][j] = self.ground_percent.pop(0)
                        count_of_lands_first_continent -= 1

        for _ in range(c):
            row = []
            for j in range(b):
                row.append('~')
            second_continent.append(row)

        for i in range(len(second_continent)):
            for j in range(len(second_continent[i])):
                if (len(second_continent) // 3) <= i <= len(second_continent) - len(second_continent) // 2.5:
                    if len(second_continent[i]) // 3 <= j <= len(second_continent[i]) // 2:
                        if not self.ground_percent:
                            break
                        second_continent[i][j] = self.ground_percent.pop(0)
                        count_of_lands_second_continent -= 1

        while count_of_lands_second_continent:
            for i in range(len(second_continent)):
                for j in range(len(second_continent[i])):
                    chance = random.randint(0, 2)
                    if not count_of_lands_second_continent:
                        break
                    if not chance:
                        second_continent[i][j] = self.ground_percent.pop(0)
                        count_of_lands_second_continent -= 1

        for i in range(len(self.map)):
            self.map[i] = first_continent[i] + second_continent[i]

        return self.map

    def show_map(self):
        for row in self.map:
            print(row)


if __name__ == '__main__':
    start()
