from typing import List, Tuple, TypeVar


Numeric = TypeVar("Numeric", int, float)


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.values = [0] * rows * cols

    def __getitem__(self, item: Tuple[int, int]):
        return self.values[self.coordinate_to_index(item)]

    def __setitem__(self, key: Tuple[int, int], new_value: Numeric):
        self.values = [
            v if i != self.coordinate_to_index(key) else new_value
            for i, v in enumerate(self.values)
        ]

    def __str__(self):
        cols_fmt = "\t".join(["{:10f}"] * self.cols)
        return "\n".join(
            cols_fmt.format(*self.row_as_list(row_n)).strip()
            for row_n in range(self.rows)
        )

    def coordinate_to_index(self, coord_tuple: Tuple[int, int]) -> int:
        row, col = coord_tuple
        return row * self.cols + col

    def row_as_list(self, n: int) -> List[int]:
        start = self.coordinate_to_index((n, 0))
        return self.values[start : start + self.cols]

    def col_as_list(self, n: int) -> List[int]:
        start = self.coordinate_to_index((0, n))
        stop = self.coordinate_to_index((self.rows - 1, n + 1))
        return self.values[start : stop : self.cols]
