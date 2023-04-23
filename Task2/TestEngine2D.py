import pytest

import Engine2D


@pytest.fixture(scope='function')
def create_test_engine():
    test_engine = Engine2D.Engine2D()
    return test_engine


@pytest.fixture(scope='function')
def create_broken_figure():

    class BrokenFigure(Engine2D.Triangle):

        def draw(self):
            super().draw()
            raise f'Error'

    broken_figure = BrokenFigure(10, 10, 10)

    return broken_figure


class TestUnit:

    def test_engines_add_method(self, create_test_engine):
        test_figure = Engine2D.Triangle(10, 10, 10)

        create_test_engine.add(test_figure)

        assert create_test_engine.canvas

    def test_engines_add_not_a_figure(self, create_test_engine):
        create_test_engine.add(0)

        assert not create_test_engine.canvas

    def test_engine_set_color(self, create_test_engine):
        create_test_engine.set_color('green')

        assert create_test_engine.color == 'green'

    def test_empty_canvas(self, create_test_engine):
        create_test_engine.add(Engine2D.Triangle(10, 10, 10))
        create_test_engine.draw()

        assert not create_test_engine.canvas

    def test_draw_broken_figure(self, create_test_engine, create_broken_figure):
        create_test_engine.add(create_broken_figure)
        try:
            create_test_engine.draw()
        except Exception:
            assert len(create_test_engine.canvas) == 1

    def test_correct_name_of_figure(self):
        test_figure = Engine2D.Triangle(10, 10, 10)

        assert test_figure.name == 'Triangle'



