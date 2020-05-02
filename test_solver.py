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
