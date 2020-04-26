from solver import *


class TestMatrix:
    m: Matrix

    def setup(self):
        self.m = Matrix(3, 3)

    def test_empty_list_to_list(self):
        assert self.m.to_list_of_rows() == [[0] * 3] * 3

    def test_set_item(self):
        self.m[0, 0] = 1
        assert self.m.to_list_of_rows() == [[1, 0, 0]] + [[0] * 3] * 2
