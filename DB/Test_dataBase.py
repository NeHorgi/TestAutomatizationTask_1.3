import sqlite3

import pytest
from pytest_lazyfixture import lazy_fixture

from Precondicions import Constants


class TestDB:

    #parameters_for_test = [f'Ship-{i}' for i in range(1, Constants.ships + 1)]

    @pytest.mark.parametrize('ship', [(pytest.lazy_fixture('create_parameters_for_test'))])
    def test_check_weapon(self, ship, create_original_conn_and_cur, create_changed_conn_and_cur, create_and_fill_db, create_temporary_db):
        #ships = request.getfixturevalue(ship)
        print(ship)
        select = f'''SELECT weapon FROM ships WHERE ship = '{str(*ship)}';'''
        weapon_components = ['reload_speed', 'rotational_speed', 'diameter', 'power_volley', 'count']
        original_weapon = create_original_conn_and_cur.execute(select).fetchall()
        changed_weapon = create_changed_conn_and_cur.execute(select).fetchall()

        if original_weapon == changed_weapon:

            for component in weapon_components:

                select = f'''SELECT {component} FROM weapons WHERE weapon = '{str(*original_weapon[0])}';'''

                original_component = create_original_conn_and_cur.execute(select).fetchall()
                changed_component = create_changed_conn_and_cur.execute(select).fetchall()
                error = f"{ship}, {str(*original_weapon[0])}\n\t" \
                        f"{component}: expected {str(*original_component[0])}, was {str(*changed_component[0])}"
                assert original_component == changed_component, error

        else:

            error = f"{ship}, {str(*changed_weapon[0])}" \
                f"\n\texpected {str(*original_weapon[0])}, was " \
                f"{str(*changed_weapon[0])}"
            assert original_weapon == changed_weapon, error

    # @pytest.mark.parametrize('ship', parameters_for_test)
    # def test_check_engine(self, ship, create_original_conn_and_cur, create_changed_conn_and_cur, create_and_fill_db, create_temporary_db):
    #     select = f'''SELECT engine FROM ships WHERE ship = '{ship}';'''
    #     engine_components = ['power', 'type']
    #     original_engine = create_original_conn_and_cur.execute(select).fetchall()
    #     changed_engine = create_changed_conn_and_cur.execute(select).fetchall()
    #
    #     if original_engine == changed_engine:
    #
    #         for component in engine_components:
    #
    #             select = f'''SELECT {component} FROM engines WHERE engine = '{str(*original_engine[0])}';'''
    #
    #             original_component = create_original_conn_and_cur.execute(select).fetchall()
    #             changed_component = create_changed_conn_and_cur.execute(select).fetchall()
    #             error = f"{ship}, {str(*original_engine[0])}\n\t" \
    #                     f"{component}: expected {str(*original_component[0])}, was {str(*changed_component[0])}"
    #             assert original_component == changed_component, error
    #
    #     else:
    #
    #         error = f"{ship}, {str(*changed_engine[0])}" \
    #             f"\n\texpected {str(*original_engine[0])}, was " \
    #             f"{str(*original_engine[0])}"
    #         assert original_engine == changed_engine, error
    #
    # @pytest.mark.parametrize('ship', parameters_for_test)
    # def test_check_hull(self, ship, create_original_conn_and_cur, create_changed_conn_and_cur, create_and_fill_db, create_temporary_db):
    #     select = f'''SELECT hull FROM ships WHERE ship = '{ship}';'''
    #     hull_components = ['armor', 'type', 'capacity']
    #     original_hull = create_original_conn_and_cur.execute(select).fetchall()
    #     changed_hull = create_changed_conn_and_cur.execute(select).fetchall()
    #
    #     if original_hull == changed_hull:
    #
    #         for component in hull_components:
    #
    #             select = f'''SELECT {component} FROM hulls WHERE hull = '{str(*original_hull[0])}';'''
    #
    #             original_component = create_original_conn_and_cur.execute(select).fetchall()
    #             changed_component = create_changed_conn_and_cur.execute(select).fetchall()
    #             error = f"{ship}, {str(*original_hull[0])}\n\t" \
    #                     f"{component}: expected {str(*original_component[0])}, was {str(*changed_component[0])}"
    #             assert original_component == changed_component, error
    #
    #     else:
    #
    #         error = f"{ship}, {str(*changed_hull[0])}" \
    #             f"\n\texpected {str(*original_hull[0])}, was " \
    #             f"{str(*original_hull[0])}"
    #         assert original_hull == changed_hull, error
