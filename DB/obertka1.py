import inspect
import random
import sqlite3

from precondicions import Weapon, Constants, Hull, Engine, Ship


def get_cursor():
    conn = sqlite3.connect('ships1.db')
    return conn.cursor()


def create_table():

    conn = sqlite3.connect('ships1.db')
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


def get_table_columns_names(table):
    select = f'''PRAGMA table_info("{table}")'''
    cur = get_cursor()
    cur.execute(select)
    column_names = [i[1] for i in cur.fetchall()]
    return column_names


def get_obj_attributes(obj):
    parameters = [a for a in inspect.getmembers(obj, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
    return parameters


def get_correct_sequence_of_attributes(table, obj):
    correct_sequence = []
    sequence_of_columns = get_table_columns_names(table)
    obj_attributes = get_obj_attributes(obj)
    for column_name in sequence_of_columns:
        for obj_attribute in obj_attributes:
            if column_name == obj_attribute[0]:
                correct_sequence.append(obj_attribute[-1])
                break
    return correct_sequence


def create_selection_to_insert(table, obj):
    data = get_correct_sequence_of_attributes(table, obj)
    select = f"""INSERT INTO "{table}" VALUES{tuple(data)};"""
    return select


def create_selection_to_get_random_parameter_from_table(table, parameter):
    select = f'''SELECT {parameter} FROM {table} ORDER BY RANDOM() LIMIT 1;'''
    return select


def get_three_random_parameters(list1, list2, list3):
    result = [random.choice(list1), random.choice(list2), random.choice(list3)]
    return result


if __name__ == '__main__':
    create_table()


