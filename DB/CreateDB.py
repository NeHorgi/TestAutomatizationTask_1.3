import random
import sqlite3
from dataclasses import dataclass


class Constants:
    ships = 200
    weapons = 20
    hulls = 5
    engines = 6
    max_value_of_params = 20


@dataclass
class Ship:
    ship_name: str
    weapon: str
    hull: str
    engine: str

    def change_random_component(self):
        component = random.choice([1, 2, 3])
        if component == 1:
            self.weapon = f'Weapon-{random.randint(1, Constants.weapons)}'
            return self.weapon
        elif component == 2:
            self.hull = f'Hull-{random.randint(1, Constants.hulls)}'
            return self.hull
        else:
            self.engine = f'Engine-{random.randint(1, Constants.engines)}'
            return self.engine


@dataclass
class Weapon:
    weapon_name: str
    reload_speed: int = 0
    rotational_speed: int = 0
    diameter: int = 0
    power_volley: int = 0
    count: int = 0

    def generate_params_params(self):
        self.reload_speed = random.randint(1, Constants.max_value_of_params)
        self.rotational_speed = random.randint(1, Constants.max_value_of_params)
        self.diameter = random.randint(1, Constants.max_value_of_params)
        self.power_volley = random.randint(1, Constants.max_value_of_params)
        self.count = random.randint(1, Constants.max_value_of_params)

        return self.reload_speed, self.rotational_speed, self.diameter, self.power_volley, self.count

    def change_random_parameter(self):
        changed_parameter = random.choice([self.reload_speed, self.rotational_speed, self.diameter, self.power_volley, self.count])
        random_count = random.randint(1, Constants.max_value_of_params)

        if changed_parameter == self.reload_speed:
            self.reload_speed = random_count
            return self.reload_speed
        elif changed_parameter == self.rotational_speed:
            self.rotational_speed = random_count
            return self.rotational_speed
        elif changed_parameter == self.diameter:
            self.diameter = random_count
            return self.diameter
        elif changed_parameter == self.power_volley:
            self.power_volley = random_count
            return self.reload_speed
        else:
            self.count = random_count
            return self.count


@dataclass
class Hull:
    hull_name: str
    armor: int = 0
    type: int = 0
    capacity: int = 0

    def generate_random_params(self):
        self.armor = random.randint(1, Constants.max_value_of_params)
        self.type = random.randint(1, Constants.max_value_of_params)
        self.capacity = random.randint(1, Constants.max_value_of_params)

        return self.armor, self.type, self.capacity

    def change_random_parameter(self):
        changed_parameter = random.choice([self.armor, self.type, self.capacity])
        random_count = random.randint(1, Constants.max_value_of_params)

        if changed_parameter == self.armor:
            self.armor = random_count
            return self.armor
        elif changed_parameter == self.type:
            self.type = random_count
            return self.type
        else:
            self.capacity = random_count
            return self.capacity


@dataclass
class Engine:
    engine_name: str
    power: int = 0
    type: int = 0

    def generate_random_params(self):
        self.power = random.randint(1, Constants.max_value_of_params)
        self.type = random.randint(1, Constants.max_value_of_params)

        return self.power, self.type

    def change_random_parameter(self):
        changed_parameter = random.choice([self.power, self.type])
        random_count = random.randint(1, Constants.max_value_of_params)

        if changed_parameter == self.power:
            self.power = random_count
            return self.power
        else:
            self.type = random_count
            return self.type


def create_and_fill_db():
    conn = sqlite3.connect('ships.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS ships(
        "ship" TEXT PRIMARY KEY,
        "weapon" TEXT,
        "hull" TEXT,
        "engine" TEXT);
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS weapons(
        "weapon" TEXT PRIMARY KEY,
        "reload_speed" INTEGER, 
        "rotational_speed" INTEGER,
        "diameter" INTEGER,
        "power_volley" INTEGER,
        "count" INTEGER,
        FOREIGN KEY (weapon) REFERENCES ships (weapon));
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS engines(
        "engine" TEXT PRIMARY KEY,
        "power" INTEGER,
        "type" INTEGER,
        FOREIGN KEY (engine) REFERENCES ships (engine));
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS hulls(
        "hull" TEXT PRIMARY KEY,
        "armor" INTEGER,
        "type" INTEGER,
        "capacity" INTEGER,
        FOREIGN KEY (hull) REFERENCES ships (hull));
    ''')

    conn.commit()

    for ship_index in range(1, Constants.ships + 1):
        ship = Ship(f'Ship-{ship_index}',
                    f'Weapon-{random.randint(1, Constants.weapons)}',
                    f'Hull-{random.randint(1, Constants.hulls)}',
                    f'Engine-{random.randint(1, Constants.engines)}'
                    )
        cur.execute(f'''INSERT INTO "ships" VALUES('{ship.ship_name}',
                                                   '{ship.weapon}',
                                                   '{ship.hull}',
                                                   '{ship.engine}');''')

    for weapon_index in range(1, Constants.weapons + 1):
        weapon = Weapon(f'Weapon-{weapon_index}')
        weapon.generate_params_params()
        cur.execute(f'''INSERT INTO "weapons" VALUES('{weapon.weapon_name}',
                                                     '{weapon.reload_speed}',
                                                     '{weapon.rotational_speed}', 
                                                     '{weapon.diameter}',
                                                     '{weapon.power_volley}',
                                                     '{weapon.count}');''')

    for hull_index in range(1, Constants.hulls + 1):
        hull = Hull(f'Hull-{hull_index}')
        hull.generate_random_params()
        cur.execute(f'''INSERT INTO "hulls" VALUES('{hull.hull_name}',
                                                   '{hull.armor}', 
                                                   '{hull.type}', 
                                                   '{hull.capacity}');''')

    for engine_index in range(1, Constants.engines + 1):
        engine = Engine(f'Engine-{engine_index}')
        engine.generate_random_params()
        cur.execute(f'''INSERT INTO "engines" VALUES('{engine.engine_name}',
                                                     '{engine.power}',
                                                     '{engine.type}');''')

    conn.commit()

    return 'ships.db'





