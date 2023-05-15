import random
import inspect
import sqlite3
from dataclasses import dataclass


class Constants:
    ships = 200
    weapons = 20
    hulls = 5
    engines = 6
    max_value_of_params = 20
    weapon_models = [f'Weapon-{i}' for i in range(1, weapons + 1)]
    hull_models = [f'Hull-{i}' for i in range(1, hulls + 1)]
    engine_models = [f'Engine-{i}' for i in range(1, engines + 1)]


def create_random_value():
    value = random.randint(1, Constants.max_value_of_params)

    return value


@dataclass
class Ship:
    ship_name: str
    weapon: str
    hull: str
    engine: str

    def change_random_component(self):
        attributes = [a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
        for attribute in attributes:
            if attribute[0] == 'ship_name':
                attributes.remove(attribute)
        random_component = random.choice(attributes)
        constant_attributes = [a for a in inspect.getmembers(Constants, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
        for constant_attribute in constant_attributes:
            try:
                if random_component[1] in constant_attribute[1]:
                    setattr(self, random_component[0], random.choice(constant_attribute[1]))
                    break
            except TypeError:
                continue


@dataclass
class Weapon:
    weapon_name: str
    reload_speed: int = 0
    rotational_speed: int = 0
    diameter: int = 0
    power_volley: int = 0
    count: int = 0

    def generate_random_parameters(self):
        parameters = [a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
        for parameter in parameters:
            if type(parameter[1]) == str:
                continue
            setattr(self, parameter[0], create_random_value())

    def change_random_parameter(self):
        random_attribute = random.choice([a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))][1:])
        setattr(self, random_attribute[0], create_random_value())


@dataclass
class Hull:
    hull_name: str
    armor: int = 0
    type: int = 0
    capacity: int = 0

    def generate_random_parameters(self):
        parameters = [a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
        for parameter in parameters:
            if type(parameter[1]) == str:
                continue
            setattr(self, parameter[0], create_random_value())

    def change_random_parameter(self):
        random_attribute = random.choice([a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))][1:])
        setattr(self, random_attribute[0], create_random_value())


@dataclass
class Engine:
    engine_name: str
    power: int = 0
    type: int = 0

    def generate_random_parameters(self):
        parameters = [a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
        for parameter in parameters:
            if type(parameter[1]) == str:
                continue
            setattr(self, parameter[0], create_random_value())

    def change_random_parameter(self):
        random_attribute = random.choice([a for a in inspect.getmembers(self, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))][1:])
        setattr(self, random_attribute[0], create_random_value())


"""
conn = sqlite3.connect('ships.db')
cur = conn.cursor()

select = f'''SELECT ship FROM ships'''
parameters_for_test = []

for ship in cur.execute(select).fetchall():
    parameters_for_test.append(str(ship))
    print(type(ship))

print(parameters_for_test)
"""

# if __name__ == '__main__':
#     conn = sqlite3.connect('ships.db')
#     cur = conn.cursor()
#     parameters_for_test = []
#     select = f'''SELECT ship FROM ships;'''
#
#     for ship in cur.execute(select).fetchall():
#         parameters_for_test.append(ship)
#
#     print(parameters_for_test)
