import shutil
import sqlite3

import pytest

import CreateDB


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
        ship = CreateDB.Ship(*record)
        ship.change_random_component()
        cur.execute(f'''UPDATE "ships" 
        SET ("weapon", "hull", "engine") = 
        ("{ship.weapon}", "{ship.hull}", "{ship.engine}") 
        WHERE ship = "{ship.ship_name}";''')

    select = '''SELECT * FROM "weapons"'''
    cur.execute(select)
    records_weapons = cur.fetchall()
    for record in records_weapons:
        weapon = CreateDB.Weapon(*record)
        weapon.change_random_parameter()
        cur.execute(f'''UPDATE "weapons" 
        SET ("reload_speed", "rotational_speed", "diameter", "power_volley", "count") = 
        ("{weapon.reload_speed}", "{weapon.rotational_speed}", "{weapon.diameter}", "{weapon.power_volley}", "{weapon.count}") 
        WHERE weapon = "{weapon.weapon_name}";''')

    select = '''SELECT * FROM "hulls"'''
    cur.execute(select)
    records_hulls = cur.fetchall()
    for record in records_hulls:
        hull = CreateDB.Hull(*record)
        hull.change_random_parameter()
        cur.execute(f'''UPDATE "hulls" 
        SET ("armor", "type", "capacity") = 
        ("{hull.armor}", "{hull.type}", "{hull.capacity}") 
        WHERE hull = "{hull.hull_name}";''')

    select = '''SELECT * FROM "engines"'''
    cur.execute(select)
    records_engines = cur.fetchall()
    for record in records_engines:
        engine = CreateDB.Engine(*record)
        engine.change_random_parameter()
        cur.execute(f'''UPDATE "engines" 
        SET ("power", "type") = 
        ("{engine.power}", "{engine.type}") 
        WHERE engine = "{engine.engine_name}";''')

    conn.commit()
