import itertools

from solver import *


class TestMatrix:
    m: Matrix

    def setup(self):
        self.m = Matrix(4, 4)

    def test_get_set_item(self):
        self.m[1, 1] = 1
        assert self.m[1, 1] == 1
        for a, b in itertools.product(range(self.m.rows), range(self.m.cols)):
            if a != 1 and b != 1:
                assert self.m[a, b] == 0

    def test_row_col_as_list(self):
        self.m[1, 1] = 1
        assert list(self.m.row_n_iter(1)) == [0, 1, 0, 0]
        assert list(self.m.col_n_iter(1)) == [0, 1, 0, 0]

    @staticmethod
    def test_coordinate_to_index():
        m = Matrix(rows=4, cols=5)
        assert m.coordinate_to_index((0, 0)) == 0
        assert m.coordinate_to_index((3, 4)) == 19
        assert m.coordinate_to_index((1, 0)) == 5
        assert m.coordinate_to_index((1, 1)) == 6

    @staticmethod
    def test_transposed():
        m = Matrix(rows=2, cols=3)

        m[0, 0] = 0
        m[0, 1] = 1
        m[0, 2] = 2

        m[1, 0] = 3
        m[1, 1] = 4
        m[1, 2] = 5

        m[2, 0] = 6
        m[2, 1] = 7
        m[2, 2] = 8

        t = m.transposed()

        assert t.rows == m.cols
        assert t.cols == m.rows

        assert t[0, 0] == 0
        assert t[0, 1] == 3
        assert t[0, 2] == 6

        assert t[1, 0] == 1
        assert t[1, 1] == 4
        assert t[1, 2] == 7

        assert t[2, 0] == 2
        assert t[2, 1] == 5
        assert t[2, 2] == 8
