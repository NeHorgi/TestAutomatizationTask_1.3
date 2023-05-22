import random


def start():
    print('Введите длину карты')
    a = int(input())
    print('Введите ширину карты')
    b = int(input())
    current_map = GenerateMapFromCiv(a, b)
    current_map.create_empty_map()
    print(f'Выберите тип карты: 1 - Пангея, 2 - Острова, 3 - Континенты')
    c = input()
    if c == '1':
        current_map.create_pangea()
    elif c == '2':
        current_map.create_islands()
    elif c == '3':
        current_map.create_continents()
    current_map.show_map()


class GenerateMapFromCiv:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.ground_percent = 0.3
        self.map = []

    def create_empty_map(self):
        self.map = [['~' for _ in range(self.x)] for _ in range(self.y)]

        return self.map

    def create_pangea(self):
        """Создание одного большого куска земли располагающегося преимущественно в центральной части карты.

        land_tiles - список с тайлами земли, в соотв. с выдранными пользователем размером карты и
        соотношением суши к карте на ней.
        count_of_lands - кол-во тайлов суши
        """
        land_tiles = ['∎' for _ in range(round(self.x * self.y * self.ground_percent))]
        count_of_lands = len(land_tiles)

        """Поскольку Пангея в цивилизации это один большой кусок земли, разделенный между собой разве что проливами 
        и маленькими морями, то я беру условные 30%, с каждой стороны, гарантированной воды, а остальное пространство
        рандомно заполняю тайлами суши, дабы добиться более интересной формы земли.
        
        pangea_height_start, pangea_weight_start - индексы тайлов, 
        начиная с которых суша может может появиться в попавшей внутрь области (по высоте)
        
        pangea_height_end, pangea_weight_start  - индексы тайлов, 
        начиная с которых суша может может появиться в попавшей внутрь области (по ширине)
        """
        pangea_height_start = round(self.x * 0.3) // 2 if round(self.x * 0.3) // 2 != 0 else 1
        pangea_height_end = self.x - pangea_height_start - 1
        pangea_weight_start = round(self.y * 0.3) // 2
        pangea_weight_end = self.y - pangea_weight_start - 1 #if pangea_height_start != 1 else self.y - pangea_weight_start

        """Цикл работает до тех пор, пока существуют тайлы земли, которые можно расположить в определенной выше 
        области. Если за полный прогон цикла ни один новый тайл не был добавлен, то это значит, что в выделенной 
        области закончилось место для суши и цикл прерывается.
        """
        while count_of_lands:
            check = count_of_lands
            tiles_count = 0
            for tiles_row in self.map:
                if pangea_height_start <= tiles_count <= pangea_height_end:
                    tile_count = 0
                    for tile in tiles_row:
                        if pangea_weight_start <= tile_count <= pangea_weight_end:
                            if not land_tiles:
                                break
                            if self.map[tiles_count][tile_count] != '∎':
                                chance = random.randint(0, 2)
                                if not chance:
                                    self.map[tiles_count][tile_count] = land_tiles.pop(0)
                                    count_of_lands -= 1
                        tile_count += 1
                tiles_count += 1
            if check == count_of_lands:
                break

        return self.map

    def create_islands(self):
        """Генерация карты с большим кол-вом разбросанных в разных частях карты участков суши.

        land_tiles - список с тайлами земли, в соотв. с выдранными пользователем размером карты и
        соотношением суши к карте на ней.
        islands_in_row - кол-во суши, доступной для "нассыпи" в одном ряду тайлов
        """
        land_tiles = ['∎' for _ in range(round(self.x * self.y * self.ground_percent))]
        islands_in_row = len(land_tiles) // self.x if self.x >= self.y else len(land_tiles) // self.y

        """Цикл работает до тех пор, пока есть доступная для "нассыпи" земля."""
        while land_tiles:
            tiles_count = 0
            for tiles_row in self.map:
                island_tiles = islands_in_row
                tile_count = 0
                for tile in tiles_row:
                    chance = random.randint(0, 2)
                    if island_tiles:
                        if not land_tiles:
                            break
                        if not chance:
                            self.map[tiles_count][tile_count] = land_tiles.pop(0)
                            island_tiles -= 1
                    tile_count += 1
                tiles_count += 1

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
            print(*row)


if __name__ == '__main__':
    start()
