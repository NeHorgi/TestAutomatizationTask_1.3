import inspect

import pytest

from Precondicions import Constants, Weapon, Engine, Hull


class TestDB:

    parameters_for_test = [f'Ship-{i}' for i in range(1, Constants.ships + 1)]

    @pytest.mark.parametrize('ship', parameters_for_test)
    def test_check_weapon(self, ship, create_original_conn_and_cur, create_changed_conn_and_cur, create_and_fill_db, create_temporary_db):
        select_ship = f'''SELECT weapon FROM ships WHERE ship = '{ship}';'''
        original_weapon = create_original_conn_and_cur.execute(select_ship).fetchall()
        changed_weapon = create_changed_conn_and_cur.execute(select_ship).fetchall()

        if original_weapon == changed_weapon:

            select_weapon = f'''SELECT * FROM weapons WHERE weapon = "{str(*original_weapon[0])}";'''
            original_weapon_params = Weapon(*(create_original_conn_and_cur.execute(select_weapon).fetchall()[0]))
            changed_weapon_params = Weapon(*(create_changed_conn_and_cur.execute(select_weapon).fetchall()[0]))

            weapon_attributes = [a for a in inspect.getmembers(original_weapon_params, lambda a:
            not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__') or a[0].endswith('_name'))]

            for attribute in weapon_attributes:

                error = f"{ship}, {str(*original_weapon[0])}\n\t" \
                        f"{attribute[0]}: expected {attribute[1]}, was {changed_weapon_params.__getattribute__(attribute[0])}"
                assert attribute[1] == changed_weapon_params.__getattribute__(attribute[0]), error

        else:

            error = f"{ship}, {str(*changed_weapon[0])}" \
                f"\n\texpected {str(*original_weapon[0])}, was " \
                f"{str(*changed_weapon[0])}"
            assert original_weapon == changed_weapon, error

    @pytest.mark.parametrize('ship', parameters_for_test)
    def test_check_engine(self, ship, create_original_conn_and_cur, create_changed_conn_and_cur, create_and_fill_db, create_temporary_db):
        select_ship = f'''SELECT engine FROM ships WHERE ship = '{ship}';'''
        original_engine = create_original_conn_and_cur.execute(select_ship).fetchall()
        changed_engine = create_changed_conn_and_cur.execute(select_ship).fetchall()

        if original_engine == changed_engine:

            select_weapon = f'''SELECT * FROM engines WHERE engine = "{str(*original_engine[0])}";'''
            original_engine_params = Engine(*(create_original_conn_and_cur.execute(select_weapon).fetchall()[0]))
            changed_engine_params = Engine(*(create_changed_conn_and_cur.execute(select_weapon).fetchall()[0]))

            engine_attributes = [a for a in inspect.getmembers(original_engine_params, lambda a:
            not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__') or a[0].endswith('_name'))]

            for attribute in engine_attributes:

                error = f"{ship}, {str(*original_engine[0])}\n\t" \
                        f"{attribute[0]}: expected {attribute[1]}, was {changed_engine_params.__getattribute__(attribute[0])}"
                assert attribute[1] == changed_engine_params.__getattribute__(attribute[0]), error

        else:

            error = f"{ship}, {str(*changed_engine[0])}" \
                f"\n\texpected {str(*original_engine[0])}, was " \
                f"{str(*changed_engine[0])}"
            assert original_engine == changed_engine, error

    @pytest.mark.parametrize('ship', parameters_for_test)
    def test_check_hull(self, ship, create_original_conn_and_cur, create_changed_conn_and_cur, create_and_fill_db, create_temporary_db):
        select_ship = f'''SELECT hull FROM ships WHERE ship = '{ship}';'''
        original_hull = create_original_conn_and_cur.execute(select_ship).fetchall()
        changed_hull = create_changed_conn_and_cur.execute(select_ship).fetchall()

        if original_hull == changed_hull:

            select_weapon = f'''SELECT * FROM hulls WHERE hull = "{str(*original_hull[0])}";'''
            original_hull_params = Hull(*(create_original_conn_and_cur.execute(select_weapon).fetchall()[0]))
            changed_hull_params = Hull(*(create_changed_conn_and_cur.execute(select_weapon).fetchall()[0]))

            hull_attributes = [a for a in inspect.getmembers(original_hull_params, lambda a:
            not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__') or a[0].endswith('_name'))]

            for attribute in hull_attributes:

                error = f"{ship}, {str(*original_hull[0])}\n\t" \
                        f"{attribute[0]}: expected {attribute[1]}, was {changed_hull_params.__getattribute__(attribute[0])}"
                assert attribute[1] == changed_hull_params.__getattribute__(attribute[0]), error

        else:

            error = f"{ship}, {str(*changed_hull[0])}" \
                f"\n\texpected {str(*original_hull[0])}, was " \
                f"{str(*changed_hull[0])}"
            assert original_hull == changed_hull, error
