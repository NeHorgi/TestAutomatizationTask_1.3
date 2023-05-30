import random
import inspect

from dataclasses import dataclass


class Constants:
    ships = 200
    weapons = 20
    hulls = 5
    engines = 6
    max_value_of_params = 20


def create_random_value():
    value = random.randint(1, Constants.max_value_of_params)

    return value


@dataclass
class Ship:
    ship: str
    weapon: str = None
    hull: str = None
    engine: str = None


@dataclass
class Weapon:
    weapon: str
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
    hull: str
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
    engine: str
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

