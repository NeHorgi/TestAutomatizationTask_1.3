import pytest

import Engine2D


class TestUnit:

    def test_create_a_figures(self):
        test_figure1 = Engine2D.Triangle(10, 10, 10)
        test_figure2 = Engine2D.Rectangle(10, 10)
        test_figure3 = Engine2D.Circle((0, 0), 10)

        test_figures = [test_figure1, test_figure2, test_figure3]

        for test_figure in test_figures:
            assert isinstance(test_figure, Engine2D.Figure)

    def test_create_not_a_figure(self):
        with pytest.raises(TypeError):
            Engine2D.Triangle(10, 10)

    def test_add_a_figure_on_canvas(self):
        test_engine = Engine2D.Engine2D()
        test_figure = Engine2D.Triangle(10, 10, 10)

        test_engine.add(test_figure)

        assert test_engine.canvas[0] == test_figure

    def test_correct_type_of_added_figure(self):
        test_engine = Engine2D.Engine2D()
        test_figure = Engine2D.Triangle(10, 10, 10)

        test_engine.add(test_figure)

        assert isinstance(test_engine.canvas[0], Engine2D.Triangle)

    def test_add_not_a_figure_on_canvas(self):
        test_engine = Engine2D.Engine2D()
        test_engine.add(0)

        assert not test_engine.canvas

    def test_adding_a_lot_of_figures(self):
        test_engine = Engine2D.Engine2D()
        test_figure1 = Engine2D.Triangle(10, 10, 10)
        test_figure2 = Engine2D.Rectangle(10, 10)
        test_figure3 = Engine2D.Circle((0, 0), 10)

        test_figures = [test_figure1, test_figure2, test_figure3]

        for test_figure in test_figures:
            test_engine.add(test_figure)

        test_engine.add(0)

        assert len(test_engine.canvas) == 3

    def test_change_color(self):
        test_engine = Engine2D.Engine2D()
        test_engine.set_color('green')
        test_engine.set_color('blue')

        assert test_engine.color == 'blue'

    def test_draw_empty_canvas(self):
        test_engine = Engine2D.Engine2D()

        assert test_engine.draw() is None

    def test_correct_attributes_of_figure_on_canvas(self):
        test_engine = Engine2D.Engine2D()
        test_figure = Engine2D.Circle((0, 0), 5)

        test_engine.add(test_figure)

        assert str(test_engine.canvas[0]) == f'Circle with center in (0, 0) and 5 radius'

