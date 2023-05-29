import inspect
import sqlite3

from precondicions import Weapon, Constants


def get_cursor():
    conn = sqlite3.connect('ships1.db')
    return conn.cursor()
#
#
# def commit():
#     conn = sqlite3.connect('ships1.db')
#     return conn.commit()


def create_table():

    conn = sqlite3.connect('ships1.db')
    #cur = conn.cursor()
    cur = get_cursor()

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

    for weapon_index in range(1, Constants.weapons + 1):
        weapon = Weapon(f'Weapon-{weapon_index}')
        weapon.generate_random_parameters()
        #cur.execute(f'''INSERT INTO "weapons" VALUES('{weapon.weapon}', '{weapon.reload_speed}', '{weapon.rotational_speed}', '{weapon.diameter}', '{weapon.power_volley}', '{weapon.count}');''')
        #print(f'''INSERT INTO "weapons" VALUES('{weapon.weapon}', '{weapon.reload_speed}', '{weapon.rotational_speed}', '{weapon.diameter}', '{weapon.power_volley}', '{weapon.count}');''')
        print(create_selection_to_insert('weapons', weapon))
        cur.execute(create_selection_to_insert('weapons', weapon))
        break

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


    # cur1 = get_cursor()
    # attributes = get_correct_sequence_of_attributes(table, obj)
    # str_attributes = []
    # for attribute in attributes:
    #     str_attributes.append(str(attribute))
    # print(str_attributes)
    # table_columns_str = ''
    # for attribute in str_attributes:
    #     table_columns_str += str(attribute) + ', '
    # table_columns_str = table_columns_str[:-2]
    # print(table_columns_str)
    # select = f'''INSERT INTO "{table}" VALUES({table_columns_str});'''
    # print(select)
    # print(f"""INSERT INTO "weapons" VALUES('Weapon-1', '16', '2', '15', '10', '14');""")
    #
    # cur.execute(select)


if __name__ == '__main__':
    create_table()
    # weapon = Weapon('Weapon-1')
    # weapon.generate_random_parameters()
    # insert_into_table('weapons', weapon)
    # commit()
    # conn = sqlite3.connect('ships1.db')
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM weapons")
    # print(cur.fetchall())

