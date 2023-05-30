import inspect
import random
import sqlite3


def get_cursor():
    """Метод для получения курсора.

    :return: Курсор для доступа к оригинальной БД
    """
    conn = sqlite3.connect('ships.db')
    return conn.cursor()


def get_table_columns_names(table):
    """Метод для получения упорядоченных наименований столбцов передаваемой таблицы.

    :param table: Имя таблицы
    :return: Упорядоченный список столбцов переданной таблицы
    """
    select = f'''PRAGMA table_info("{table}")'''
    cur = get_cursor()
    cur.execute(select)
    column_names = [i[1] for i in cur.fetchall()]
    return column_names


def get_obj_attributes(obj):
    """Метод для получения аттрибутов передаваемого класса.

    :param obj: Обьект класса
    :return: Список аттрибутов переданного класса
    """
    parameters = [a for a in inspect.getmembers(obj, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
    return parameters


def get_obj_attributes_without_mane(obj):
    """Метод для получения аттрибутов передаваемого класса, без аттрибута с названием обьекта.
    Необходим для получения рандомного аттрибута, который будет изменен и занесен в новую таблицу.

    :param obj: Обьект класса
    :return: Список аттрибутов переданного класса, без аттрибута с названием обьекта
    """
    parameters = [a for a in inspect.getmembers(obj, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
    for parameter in parameters:
        if parameter[0] == 'ship':
            parameters.remove(parameter)
    return parameters


def get_random_obj_attribute(obj):
    """Метод для получения рандомного аттрибута обьекта класса (Не включая аттрибут с названием класса).

    :param obj: Обьект класса
    :return: Рандомный аттрибут переданного класса (Не включая аттрибут с названием класса)
    """
    return random.choice(get_obj_attributes_without_mane(obj))


def get_correct_sequence_of_attributes(table, obj):
    """Метод для упорядочивания аттрибутов передаваемого класса, в соотв. с порядком столбцов передаваемой
    таблицы из БД.

    :param table: Имя таблицы
    :param obj: Обьект класса
    :return: Список аттрибутов переданного класса, упорядоченный в соотв. с порядком стобцов передаваемой таблицы из БД
    """
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
    """Метод для внесения данных, состоящих из аттрибутов передаваемого класса, в передаваемую таблицы.

    :param table: Имя таблицы
    :param obj: Обьект класса
    :return: Строковый запрос в БД, с указанием имени таблицы, куда будет сделана запись, и значениями,
    являющимися упорядоченными в соотв. с порядком столбоцов в передаваемой таблице
    """
    data = get_correct_sequence_of_attributes(table, obj)
    select = f'''INSERT INTO "{table}" VALUES{tuple(data)};'''
    return select


def create_selection_to_get_random_parameter_from_table(table, parameter):
    """Метод для получения рандомного значения столбца, из указанной таблицы.

    :param table: Имя таблицы
    :param parameter: Имя столбца
    :return: Строковый запрос в БД, с указанием имени таблицы, от куда будет получено одно рандомное значение,
    пиз передаваемого столбца
    """
    select = f'''SELECT {parameter} FROM {table} ORDER BY RANDOM() LIMIT 1;'''
    return select


def get_three_random_parameters(list1, list2, list3):
    """Метод для получения списка, состоящего из трех рандомных значений, полученных из трех разных списков.
    Метод был написан для того, чтобы сократить кол-во обращений в БД, на этапе заполнения таблицы с кораблями,
    при генерации оригинальной БД.

    :param list1: Список с моделями орудий
    :param list2: Список с моделями двигателей
    :param list3: Список с моделями корпусов
    :return: Список из трех рандомных моделей оридий, двигателей и корпусов. По сути, это список из
    компанентов конкретного корабля.
    """
    result = [random.choice(list1), random.choice(list2), random.choice(list3)]
    return result


