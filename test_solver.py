from solver import *


class TestMatrix:
    m: Matrix

    def setup(self):
        self.m = Matrix(3, 3)

    def test_empty_list_to_list(self):
        assert self.m.to_list_of_lists() == [[0] * 3] * 3

    def test_set_item(self):
        self.m[0, 0] = 1
        assert self.m.to_list_of_lists() == [[1, 0, 0]] + [[0] * 3] * 2

    def test_str(self):
        self.m[0, 0] = 5000
        print(self.m)
        assert (
            str(self.m) == "5000.000000       0.000000        0.000000\n"
            "0.000000          0.000000        0.000000\n"
            "0.000000          0.000000        0.000000"
        )
