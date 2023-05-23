import random


def start():
    print('Введите длину карты')
    a = int(input())
    print('Введите ширину карты')
    b = int(input())
    current_map = CreatingMapFromCiv(a, b)
    current_map.create_empty_map()
    print(f'Выберите тип карты: 1 - Пангея, 2 - Острова, 3 - Континенты')
    c = input()
    if current_map.create_tiny_map():
        current_map.create_tiny_map()
        current_map.show_map()
        return
    if c == '1':
        current_map.create_pangea()
    elif c == '2':
        current_map.create_islands()
    elif c == '3':
        current_map.create_continents()
    current_map.show_map()


class CreatingMapFromCiv:

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
        """Генерация карты с несколькими относительно большими участками суши, разделенными между собой морями
        и проливами.

        height_border_top, height_border_bot - границы по высоте "зассыпаемой" землей части карты.
        Беру 30% воды суммарно (и с нижнего края, и с верхнего) в границах полюсов.

        first_continent_area_start, first_continent_area_end - границы по ширине "зассыпаемой" землей части
        карты под первый континент.
        second_continent_area_start, second_continent_area_end - границы по ширине "зассыпаемой" землей части
        карты под второй континент.

        count_of_lands_first_continent, count_of_lands_second_continent - кол-во тайлов земли для
        первого и второго континентов (для двух разных циклов)
        first_continent_land_tiles, second_continent_land_tiles - списки с тайлами земли (так же
        для двух разных циклов)
        """
        height_border_top = round(self.x * 0.3) // 2
        height_border_bot = self.x - height_border_top - 1

        first_continent_area_start = 0
        first_continent_area_end = self.y // 2
        second_continent_area_start = self.y // 2
        second_continent_area_end = self.y - 1

        count_of_lands_first_continent = round(self.x * self.y * self.ground_percent // 2)
        count_of_lands_second_continent = count_of_lands_first_continent
        first_continent_land_tiles = ['∎' for _ in range(count_of_lands_first_continent)]
        second_continent_land_tiles = ['∎' for _ in range(count_of_lands_second_continent)]

        """Циклы определяют для себя кусок карты, в котором будут работать. Далее, в ранее отобранном 
        куске, они определяют для себя "рабочую" область, где и генерят несколько относительно 
        больших кусков земли.
        На случай малых масштабов карты, или долгих провисаний циклов из-за необычных конфигураций
        карты, добавлен счетчик, который принудительно завершит цикл.
        """
        while count_of_lands_first_continent:
            check = 0
            tiles_count = 0
            for tiles_row in self.map:
                if height_border_top <= tiles_count <= height_border_bot:
                    tile_count = 0
                    for tile in tiles_row:
                        if tile_count > first_continent_area_end:
                            break
                        if first_continent_area_start <= tile_count < first_continent_area_end:
                            if not first_continent_land_tiles:
                                break
                            chance = random.randint(0, 2)
                            if not chance:
                                if self.map[tiles_count][tile_count] != '∎':
                                    self.map[tiles_count][tile_count] = first_continent_land_tiles.pop(0)
                                    count_of_lands_first_continent -= 1
                        tile_count += 1
                tiles_count += 1
                check += 1
            if check == 100:
                break

        while count_of_lands_second_continent:
            check = 0
            tiles_count = 0
            for tiles_row in self.map:
                if height_border_top <= tiles_count <= height_border_bot:
                    tile_count = 0
                    for tile in tiles_row:
                        if second_continent_area_start < tile_count <= second_continent_area_end:
                            if not second_continent_land_tiles:
                                break
                            chance = random.randint(0, 2)
                            if not chance:
                                if self.map[tiles_count][tile_count] != '∎':
                                    self.map[tiles_count][tile_count] = second_continent_land_tiles.pop(0)
                                    count_of_lands_second_continent -= 1
                        tile_count += 1
                tiles_count += 1
                check += 1
            if check == 100:
                break

        return self.map

    def create_tiny_map(self):
        """Данная функция присутсвует тут только для того, чтобы обработать варианты, когда пользавателем
        задаются слишком маленькие параметры для создания карты.
        Соотв. для крошечной карты нет никаких отличий между континентами, остравами и тд.,
        поэтому она генерируется абсолютно рандомно.
        """
        if self.x <= 2 or self.y <= 2:
            land_tiles = ['∎' for _ in range(round(self.x * self.y * self.ground_percent))]
            while land_tiles:
                tiles_count = 0
                for tiles_row in self.map:
                    tile_count = 0
                    for tile in tiles_row:
                        if not land_tiles:
                            break
                        chance = random.randint(0, 2)
                        if not chance:
                            self.map[tiles_count][tile_count] = land_tiles.pop(0)
                        tile_count += 1
                    tiles_count += 1

            return self.map

    def show_map(self):
        for row in self.map:
            print(*row)


if __name__ == '__main__':
    start()
