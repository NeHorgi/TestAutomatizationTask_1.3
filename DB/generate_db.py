import random
import sqlite3

from obertka import create_selection_to_insert, get_three_random_parameters
from precondicions import Constants, Ship, Weapon, Hull, Engine


def create_and_fill_db():

    conn = sqlite3.connect('ships.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS ships(
        "ship" TEXT PRIMARY KEY,
        "weapon" TEXT,
        "hull" TEXT,
        "engine" TEXT);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS weapons(
        "weapon" TEXT PRIMARY KEY,
        "reload_speed" INTEGER, 
        "rotational_speed" INTEGER,
        "diameter" INTEGER,
        "power_volley" INTEGER,
        "count" INTEGER,
        FOREIGN KEY (weapon) REFERENCES ships (weapon));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS engines(
        "engine" TEXT PRIMARY KEY,
        "power" INTEGER,
        "type" INTEGER,
        FOREIGN KEY (engine) REFERENCES ships (engine));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS hulls(
        "hull" TEXT PRIMARY KEY,
        "armor" INTEGER,
        "type" INTEGER,
        "capacity" INTEGER,
        FOREIGN KEY (hull) REFERENCES ships (hull));''')

    for weapon_index in range(1, Constants.weapons + 1):
        weapon = Weapon(f'Weapon-{weapon_index}')
        weapon.generate_random_parameters()
        cur.execute(create_selection_to_insert('weapons', weapon))

    for hull_index in range(1, Constants.hulls + 1):
        hull = Hull(f'Hull-{hull_index}')
        hull.generate_random_parameters()
        cur.execute(create_selection_to_insert('hulls', hull))

    for engine_index in range(1, Constants.engines + 1):
        engine = Engine(f'Engine-{engine_index}')
        engine.generate_random_parameters()
        cur.execute(create_selection_to_insert('engines', engine))

    """
    Три запроса и последующее создание трех списков с моделями орудий, двигателей и корпусов сделано для 
    сокращения обращений в БД.
    """

    weapons_select = f'''SELECT weapon FROM weapons'''
    weapons_from_db = cur.execute(weapons_select).fetchall()

    engines_select = f'''SELECT engine FROM engines'''
    engines_from_db = cur.execute(engines_select).fetchall()

    hulls_select = f'''SELECT hull FROM hulls'''
    hulls_from_db = cur.execute(hulls_select).fetchall()

    for ship_index in range(1, Constants.ships + 1):
        ship_construction = [f'Ship-{ship_index}']
        for parameter in get_three_random_parameters(weapons_from_db, hulls_from_db, engines_from_db):
            ship_construction.append(*parameter)
        ship = Ship(*ship_construction)
        cur.execute(create_selection_to_insert('ships', ship))

    conn.commit()


if __name__ == '__main__':
    create_and_fill_db()



