import random
import sqlite3

from CreateDB import create_and_fill_db


def create_temporary_db(db):
    data_base = db
    conn = sqlite3.connect(data_base)
    cur = conn.cursor()

    cur.execute('''ATTACH DATABASE 'C:\code\AutomatizationTaskRework\OldOne\changed_ships_db' AS changed_ships;''')
    conn.commit()

    cur.execute('''CREATE TABLE changed_ships.ships(
        ship TEXT PRIMARY KEY,
        weapon TEXT,
        hull TEXT,
        engine TEXT);    
    ''')

    cur.execute('''INSERT INTO changed_ships.ships SELECT ship, weapon, hull, engine FROM ships;''')

    conn.commit()

    cur.execute('''CREATE TABLE changed_ships.engines(
        engine TEXT PRIMARY KEY,
        power INTEGER,
        type INTEGER);
    ''')

    cur.execute('''INSERT INTO changed_ships.engines SELECT engine, power, type FROM engines;''')

    cur.execute('''CREATE TABLE changed_ships.weapons(
        weapon TEXT PRIMARY KEY,
        reload_speed INTEGER, 
        rotational_speed INTEGER,
        diameter INTEGER,
        power_volley INTEGER,
        count INTEGER);
    ''')

    cur.execute('''INSERT INTO changed_ships.weapons SELECT
    weapon, reload_speed, rotational_speed, diameter, power_volley, count FROM weapons;
    ''')

    cur.execute('''CREATE TABLE changed_ships.hulls(
        hull TEXT PRIMARY KEY,
        armor INTEGER,
        type INTEGER,
        capacity INTEGER);
    ''')

    cur.execute('''INSERT INTO changed_ships.hulls SELECT
    hull, armor, type, capacity FROM hulls;
    ''')

    conn.commit()

    conn1 = sqlite3.connect('changed_ships_db')
    cur1 = conn1.cursor()

    ships_need_to_be_changed = [f'Ship-{i}' for i in range(1, 201)]
    weapons_need_to_be_changed = [f'Weapon-{i}' for i in range(1, 21)]
    hulls_need_to_be_changed = [f'Hull-{i}' for i in range(1, 6)]
    engines_need_to_be_changed = [f'Engine-{i}' for i in range(1, 7)]

    for changed_ship in ships_need_to_be_changed:
        column = random.randint(1, 3)
        if column == 1:
            cur1.execute(
                f'''UPDATE ships SET weapon = '{random.choice(weapons_need_to_be_changed)}' WHERE ship = '{changed_ship}';''')
        elif column == 2:
            cur1.execute(
                f'''UPDATE ships SET hull = '{random.choice(hulls_need_to_be_changed)}' WHERE ship = '{changed_ship}';''')
        elif column == 3:
            cur1.execute(
                f'''UPDATE ships SET engine = '{random.choice(engines_need_to_be_changed)}' WHERE ship = '{changed_ship}';''')
        conn1.commit()

    for changed_weapon in weapons_need_to_be_changed:
        column = random.randint(1, 5)
        if column == 1:
            cur1.execute(
                f'''UPDATE weapons SET reload_speed = '{random.randint(1, 20)}' WHERE weapon = '{changed_weapon}';''')
        elif column == 2:
            cur1.execute(
                f'''UPDATE weapons SET rotational_speed = '{random.randint(1, 20)}' WHERE weapon = '{changed_weapon}';''')
        elif column == 3:
            cur1.execute(
                f'''UPDATE weapons SET diameter = '{random.randint(1, 20)}' WHERE weapon = '{changed_weapon}';''')
        elif column == 4:
            cur1.execute(
                f'''UPDATE weapons SET power_volley = '{random.randint(1, 20)}' WHERE weapon = '{changed_weapon}';''')
        elif column == 5:
            cur1.execute(f'''UPDATE weapons SET count = '{random.randint(1, 20)}' WHERE weapon = '{changed_weapon}';''')
        conn1.commit()

    for changed_hull in hulls_need_to_be_changed:
        column = random.randint(1, 3)
        if column == 1:
            cur1.execute(f'''UPDATE hulls SET armor = '{random.randint(1, 20)}' WHERE hull = '{changed_hull}';''')
        elif column == 2:
            cur1.execute(f'''UPDATE hulls SET type = '{random.randint(1, 20)}' WHERE hull = '{changed_hull}';''')
        elif column == 3:
            cur1.execute(f'''UPDATE hulls SET capacity = '{random.randint(1, 20)}' WHERE hull = '{changed_hull}';''')
        conn1.commit()

    for changed_engine in engines_need_to_be_changed:
        column = random.randint(1, 2)
        if column == 1:
            cur1.execute(f'''UPDATE engines SET power = '{random.randint(1, 20)}' WHERE engine = '{changed_engine}';''')
        elif column == 2:
            cur1.execute(f'''UPDATE engines SET type = '{random.randint(1, 20)}' WHERE engine = '{changed_engine}';''')
        conn1.commit()


create_temporary_db(create_and_fill_db())
