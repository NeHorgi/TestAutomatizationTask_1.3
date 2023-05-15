import random
import shutil
import sqlite3

import pytest

from Precondicions import Constants
from Precondicions import Ship, Weapon, Hull, Engine


@pytest.fixture(scope='session')
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
        weapon.generate_random_parameters()
        cur.execute(f'''INSERT INTO "weapons" VALUES('{weapon.weapon_name}',
                                                     '{weapon.reload_speed}',
                                                     '{weapon.rotational_speed}', 
                                                     '{weapon.diameter}',
                                                     '{weapon.power_volley}',
                                                     '{weapon.count}');''')

    for hull_index in range(1, Constants.hulls + 1):
        hull = Hull(f'Hull-{hull_index}')
        hull.generate_random_parameters()
        cur.execute(f'''INSERT INTO "hulls" VALUES('{hull.hull_name}',
                                                   '{hull.armor}', 
                                                   '{hull.type}', 
                                                   '{hull.capacity}');''')

    for engine_index in range(1, Constants.engines + 1):
        engine = Engine(f'Engine-{engine_index}')
        engine.generate_random_parameters()
        cur.execute(f'''INSERT INTO "engines" VALUES('{engine.engine_name}',
                                                     '{engine.power}',
                                                     '{engine.type}');''')

    conn.commit()


@pytest.fixture(scope='session')
def create_temporary_db():
    original_db = 'ships.db'
    copied_db = 'changed_ships.db'

    shutil.copy(original_db, copied_db)

    conn = sqlite3.connect('changed_ships.db')
    cur = conn.cursor()

    select = '''SELECT * FROM "ships"'''
    cur.execute(select)
    records_ships = cur.fetchall()
    for record in records_ships:
        ship = Ship(*record)
        ship.change_random_component()
        cur.execute(f'''UPDATE "ships" 
        SET ("weapon", "hull", "engine") = 
        ("{ship.weapon}", "{ship.hull}", "{ship.engine}") 
        WHERE ship = "{ship.ship_name}";''')

    select = '''SELECT * FROM "weapons"'''
    cur.execute(select)
    records_weapons = cur.fetchall()
    for record in records_weapons:
        weapon = Weapon(*record)
        weapon.change_random_parameter()
        cur.execute(f'''UPDATE "weapons" 
        SET ("reload_speed", "rotational_speed", "diameter", "power_volley", "count") = 
        ("{weapon.reload_speed}", "{weapon.rotational_speed}", "{weapon.diameter}", "{weapon.power_volley}", "{weapon.count}") 
        WHERE weapon = "{weapon.weapon_name}";''')

    select = '''SELECT * FROM "hulls"'''
    cur.execute(select)
    records_hulls = cur.fetchall()
    for record in records_hulls:
        hull = Hull(*record)
        hull.change_random_parameter()
        cur.execute(f'''UPDATE "hulls" 
        SET ("armor", "type", "capacity") = 
        ("{hull.armor}", "{hull.type}", "{hull.capacity}") 
        WHERE hull = "{hull.hull_name}";''')

    select = '''SELECT * FROM "engines"'''
    cur.execute(select)
    records_engines = cur.fetchall()
    for record in records_engines:
        engine = Engine(*record)
        engine.change_random_parameter()
        cur.execute(f'''UPDATE "engines" 
        SET ("power", "type") = 
        ("{engine.power}", "{engine.type}") 
        WHERE engine = "{engine.engine_name}";''')

    conn.commit()


@pytest.fixture(scope='function')
def create_original_conn_and_cur():
    conn = sqlite3.connect('ships.db')
    cur = conn.cursor()

    return cur


@pytest.fixture(scope='function')
def create_changed_conn_and_cur():
    conn_changed = sqlite3.connect('changed_ships.db')
    cur_changed = conn_changed.cursor()

    return cur_changed


@pytest.fixture(scope='session')
def create_parameters_for_test(create_and_fill_db):
    conn = sqlite3.connect('ships.db')
    cur = conn.cursor()
    parameters_for_test = []
    select = f'''SELECT ship FROM ships;'''

    for ship in cur.execute(select).fetchall():
        parameters_for_test.append(ship)
        yield ship


