import random


class GenerateMapFromCiv:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ground_percent = ['∎' for _ in range(round(self.x * self.y * 0.3))]
        self.map = [['~' for _ in range(self.x)] for _ in range(self.y)]

    def create_pangea(self):
        pangea = []
        pangea_x = round(self.x / 1.4)
        pangea_y = round(self.y / 1.4)
        for i in range(pangea_x):
            row = []
            for j in range(pangea_y):
                row.append('~')
            pangea.append(row)

        for i in range(len(pangea)):
            for j in range(len(pangea[i])):
                if (len(pangea) // 2.5) <= i < len(pangea) - len(pangea) // 2.5:
                    if (len(pangea) // 2.5) <= j < len(pangea) - len(pangea) // 2.5:
                        pangea[i][j] = self.ground_percent.pop()

        for i in range(len(pangea)):
            for j in range(len(pangea[i])):
                chance = random.randint(0, 1)
                if chance:
                    if pangea[i][j] == '~':
                        try:
                            pangea[i][j] = self.ground_percent.pop(0)
                        except IndexError:
                            break

        row = 0
        for i in range(len(self.map)):
            if self.x // 2 - pangea_x // 2 <= i <= self.x // 2 + pangea_x // 2:
                try:
                    self.map[i][self.y // 2 - pangea_y // 2:(self.y // 2 + pangea_y // 2)] = pangea[row]
                    if len(self.map[i]) > len(self.map[i - 1]):
                        self.map[i].pop(-1)
                    row += 1
                except IndexError:
                    break

        return self.map

    def create_islands(self):
        if self.x >= self.y:
            islands_in_row = len(self.ground_percent) // self.x
        else:
            islands_in_row = len(self.ground_percent) // self.y

        for row in range(len(self.map)):
            current_islands = islands_in_row
            for tile in range(len(self.map[row])):
                chance = random.randint(0, 2)
                if current_islands:
                    if not chance:
                        self.map[row][tile] = '∎'
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



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    CurrentMap = GenerateMapFromCiv(a, b)
    #for i in CurrentMap.create_pangea():
    #    print(i)
    for i in CurrentMap.create_islands():
        print(i)
