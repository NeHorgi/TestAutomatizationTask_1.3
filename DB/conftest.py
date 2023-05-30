import shutil
import sqlite3

import pytest

from obertka import get_random_obj_attribute, create_selection_to_get_random_parameter_from_table
from precondicions import Ship, Weapon, Hull, Engine


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
        random_attribute = get_random_obj_attribute(ship)
        new_value = str(*cur.execute(create_selection_to_get_random_parameter_from_table(random_attribute[0]+'s', random_attribute[0])).fetchall()[0])
        setattr(ship, random_attribute[0], new_value)
        cur.execute(f'''UPDATE "ships"
        SET ("weapon", "hull", "engine") =
        ("{ship.weapon}", "{ship.hull}", "{ship.engine}")
        WHERE ship = "{ship.ship}";''')

    select = '''SELECT * FROM "weapons"'''
    cur.execute(select)
    records_weapons = cur.fetchall()
    for record in records_weapons:
        weapon = Weapon(*record)
        weapon.change_random_parameter()
        cur.execute(f'''UPDATE "weapons"
        SET ("reload_speed", "rotational_speed", "diameter", "power_volley", "count") =
        ("{weapon.reload_speed}", "{weapon.rotational_speed}", "{weapon.diameter}", "{weapon.power_volley}", "{weapon.count}")
        WHERE weapon = "{weapon.weapon}";''')

    select = '''SELECT * FROM "hulls"'''
    cur.execute(select)
    records_hulls = cur.fetchall()
    for record in records_hulls:
        hull = Hull(*record)
        hull.change_random_parameter()
        cur.execute(f'''UPDATE "hulls"
        SET ("armor", "type", "capacity") =
        ("{hull.armor}", "{hull.type}", "{hull.capacity}")
        WHERE hull = "{hull.hull}";''')

    select = '''SELECT * FROM "engines"'''
    cur.execute(select)
    records_engines = cur.fetchall()
    for record in records_engines:
        engine = Engine(*record)
        engine.change_random_parameter()
        cur.execute(f'''UPDATE "engines"
        SET ("power", "type") =
        ("{engine.power}", "{engine.type}")
        WHERE engine = "{engine.engine}";''')

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


def create_parameters():
    conn = sqlite3.connect('ships.db')
    cur = conn.cursor()
    select = f'''SELECT ship FROM ships;'''
    parameter_for_test = cur.execute(select).fetchall()

    return parameter_for_test


def pytest_generate_tests(metafunc):
    if 'ship' in metafunc.fixturenames:
        metafunc.parametrize('ship', create_parameters())
