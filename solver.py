from collections import defaultdict
from typing import Iterator, Tuple, TypeVar


Numeric = TypeVar("Numeric", int, float)


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self._values_store = defaultdict(lambda: 0)

    def __getitem__(self, item: Tuple[int, int]):
        return self._values_store[item]

    def __setitem__(self, key: Tuple[int, int], new_value: Numeric):
        self._values_store[key] = new_value

    def __str__(self):
        cols_fmt = "\t".join(["{:10f}"] * self.cols)
        return "\n".join(
            cols_fmt.format(*self.row_n_iter(row_n)).strip()
            for row_n in range(self.rows)
        )

    def coordinate_to_index(self, coord_tuple: Tuple[int, int]) -> int:
        row, col = coord_tuple
        return row * self.cols + col

    def row_n_iter(self, n: int) -> Iterator[int]:
        return (self._values_store[n, col] for col in range(self.cols))

    def col_n_iter(self, n: int) -> Iterator[int]:
        return (self._values_store[row, n] for row in range(self.rows))
