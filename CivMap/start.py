from civmap import CreatingMapFromCiv


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


if __name__ == '__main__':
    start()
