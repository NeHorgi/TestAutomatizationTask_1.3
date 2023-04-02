import random
import sqlite3


def create_and_fill_db():
    conn = sqlite3.connect('ships.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS ships(
        ship TEXT PRIMARY KEY,
        weapon TEXT,
        hull TEXT,
        engine TEXT);
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS weapons(
        weapon TEXT PRIMARY KEY,
        reload_speed INTEGER, 
        rotational_speed INTEGER,
        diameter INTEGER,
        power_volley INTEGER,
        count INTEGER,
        FOREIGN KEY (weapon) REFERENCES ships (weapon));
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS engines(
        engine TEXT PRIMARY KEY,
        power INTEGER,
        type INTEGER,
        FOREIGN KEY (engine) REFERENCES ships (engine));
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS hulls(
        hull TEXT PRIMARY KEY,
        armor INTEGER,
        type INTEGER,
        capacity INTEGER,
        FOREIGN KEY (hull) REFERENCES ships (hull));
    ''')

    conn.commit()

    for i in range(1, 21):
        weapon = [random.randint(1, 20) for i in range(5)]
        weapon.insert(0, f'Weapon-{i}')
        cur.execute('''INSERT INTO weapons VALUES(?,?,?,?,?,?);''', weapon)
        conn.commit()

    for i in range(1, 6):
        hull = [random.randint(1, 20) for i in range(3)]
        hull.insert(0, f'Hull-{i}')
        cur.execute('''INSERT INTO hulls VALUES(?,?,?,?);''', hull)
        conn.commit()

    for i in range(1, 7):
        engine = [random.randint(1, 20) for i in range(2)]
        engine.insert(0, f'Engine-{i}')
        cur.execute('''INSERT INTO engines VALUES(?,?,?);''', engine)
        conn.commit()

    for i in range(1, 201):
        ship = [f'Ship-{i}']
        cur.execute('''SELECT * FROM weapons''')
        ship.append(random.choice(cur.fetchall())[0])
        cur.execute('''SELECT * FROM hulls''')
        ship.append(random.choice(cur.fetchall())[0])
        cur.execute('''SELECT * FROM engines''')
        ship.append(random.choice(cur.fetchall())[0])
        cur.execute('''INSERT INTO ships VALUES(?,?,?,?);''', ship)
        conn.commit()

    return 'ships.db'



