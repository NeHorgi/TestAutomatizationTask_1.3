class Figure:

    def __init__(self, name: str):
        self.name = name


class Triangle(Figure):

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(self.__class__.__name__)

    def __repr__(self):
        return f'{self.name} with {self.a}, {self.b} and {self.c} sides'

    def draw(self):
        print(f'Drawing {self.name}: {self.__repr__()}')


class Rectangle(Figure):

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        super().__init__(self.__class__.__name__)

    def __repr__(self):
        return f'{self.name} with {self.a} and {self.b} sides'

    def draw(self):
        #raise f'Тестовое багло'
        print(f'Drawing {self.name}: {self.__repr__()}')


class Circle(Figure):

    def __init__(self, center: tuple, radius: int):
        self.center = center
        self.radius = radius
        super().__init__(self.__class__.__name__)

    def __repr__(self):
        return f'{self.name} with center in {self.center} and {self.radius} radius'

    def draw(self):
        print(f'Drawing {self.name}: {self.__repr__()}')


class Engine2D:

    def __init__(self):
        self.color = None
        self.canvas = []

    def add(self, obj: Figure):
        if isinstance(obj, Figure):
            self.canvas.append(obj)

    def draw(self):
        if not self.canvas:
            return None
        while self.canvas:
            try:
                self.canvas[0].draw(), print(f'{self.color} color' if self.color else f'')
                self.canvas.pop(0)
            except Exception:
                print(f'Что-то пошло не так, отрисовка фигуры невозможна.')
                self.canvas[0].draw()

                #Hа случай, если нужно продолжать работу, при возникновении ошибки:
                
                #print(f'Что-то пошло не так, отрисовка фигуры невозможна.')
                #self.canvas.pop(0)

    def set_color(self, color: str):
        self.color = color


if __name__ == '__main__':
    engine = Engine2D()
    tr = Triangle(10, 10, 10)
    cr = Circle((0, 0), 5)
    rc = Rectangle(10, 10)
    engine.add(tr)
    engine.add(cr)
    engine.set_color('green')
    engine.add(rc)
    engine.add(tr)
    engine.set_color('blue')
    engine.draw()



