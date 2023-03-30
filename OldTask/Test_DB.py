import pytest
import sqlite3

from CreateDB import create_and_fill_db
from CreateTemporaryDB import create_temporary_db


conn_ships = sqlite3.connect(create_and_fill_db())
conn_changed_weapons = sqlite3.connect(create_temporary_db())

cur = conn_ships.cursor()
cur_changed = conn_changed_weapons.cursor()

parameters_for_test = [f'Ship-{i}' for i in range(1, 201)]


@pytest.mark.parametrize('ship', parameters_for_test)
def test_check_weapon(ship):
    weapon_components = ['reload_speed', 'rotational_speed', 'diameter', 'power_volley', 'count']
    original_weapon = cur.execute(f'''SELECT weapon FROM ships WHERE ship = '{ship}';''').fetchall()
    changed_weapon = cur_changed.execute(f'''SELECT weapon FROM ships WHERE ship = '{ship}';''').fetchall()

    if original_weapon == changed_weapon:

        for component in weapon_components:

            original_component = cur.execute(f'''SELECT {component} FROM weapons WHERE weapon = '{str(*original_weapon[0])}';''').fetchall()
            changed_component = cur_changed.execute(f'''SELECT {component} FROM weapons WHERE weapon = '{str(*original_weapon[0])}';''').fetchall()
            error = f"{ship}, {str(*original_component[0])}\n\t" \
                    f"{component}: expected {str(*original_component[0])}, was {str(*changed_component[0])}"
            assert original_component == changed_component, error

    else:

        error = f"{ship}, {str(*changed_weapon[0])}" \
            f"\n\texpected {str(*original_weapon[0])}, was " \
            f"{str(*changed_weapon[0])}"
        assert original_weapon == changed_weapon, error


@pytest.mark.parametrize('ship', parameters_for_test)
def test_check_engine(ship):
    engine_components = ['power', 'type']
    original_engine = cur.execute(f'''SELECT engine FROM ships WHERE ship = '{ship}';''').fetchall()
    changed_engine = cur_changed.execute(f'''SELECT engine FROM ships WHERE ship = '{ship}';''').fetchall()

    if original_engine == changed_engine:

        for component in engine_components:

            original_component = cur.execute(f'''SELECT {component} FROM engines WHERE engine = '{str(*original_engine[0])}';''').fetchall()
            changed_component = cur_changed.execute(f'''SELECT {component} FROM engines WHERE engine = '{str(*original_engine[0])}';''').fetchall()
            error = f"{ship}, {str(*original_component[0])}\n\t" \
                    f"{component}: expected {str(*original_component[0])}, was {str(*changed_component[0])}"
            assert original_component == changed_component, error

    else:

        error = f"{ship}, {str(*changed_engine[0])}" \
            f"\n\texpected {str(*original_engine[0])}, was " \
            f"{str(*original_engine[0])}"
        assert original_engine == changed_engine, error


@pytest.mark.parametrize('ship', parameters_for_test)
def test_check_hull(ship):
    hull_components = ['armor', 'type', 'capacity']
    original_hull = cur.execute(f'''SELECT hull FROM ships WHERE ship = '{ship}';''').fetchall()
    changed_hull = cur_changed.execute(f'''SELECT hull FROM ships WHERE ship = '{ship}';''').fetchall()

    if original_hull == changed_hull:

        for component in hull_components:

            original_component = cur.execute(f'''SELECT {component} FROM hulls WHERE hull = '{str(*original_hull[0])}';''').fetchall()
            changed_component = cur_changed.execute(f'''SELECT {component} FROM hulls WHERE hull = '{str(*original_hull[0])}';''').fetchall()
            error = f"{ship}, {str(*original_component[0])}\n\t" \
                    f"{component}: expected {str(*original_component[0])}, was {str(*changed_component[0])}"
            assert original_component == changed_component, error

    else:

        error = f"{ship}, {str(*changed_hull[0])}" \
            f"\n\texpected {str(*original_hull[0])}, was " \
            f"{str(*original_hull[0])}"
        assert original_hull == changed_hull, error
