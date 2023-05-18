import random
import sqlite3

from Precondicions import Constants, Ship, Weapon, Hull, Engine


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


if __name__ == '__main__':
    create_and_fill_db()



