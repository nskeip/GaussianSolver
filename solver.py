from collections import defaultdict
from typing import Iterator, Optional, Tuple, TypeVar


Numeric = TypeVar("Numeric", int, float)
CoordinatePair = Tuple[int, int]


class Matrix:
    def __init__(self, rows: int, cols: int, store: Optional[defaultdict] = None):
        self.rows = rows
        self.cols = cols
        self._values_store = store or defaultdict(int)

    def __getitem__(self, item: CoordinatePair):
        return self._values_store[item]

    def __setitem__(self, key: CoordinatePair, new_value: Numeric):
        self._values_store[key] = new_value

    def __str__(self):
        cols_fmt = "\t".join(["{:10f}"] * self.cols)
        return "\n".join(
            cols_fmt.format(*self.row_n_iter(row_n)).strip()
            for row_n in range(self.rows)
        )

    def coordinate_to_index(self, coord_pair: CoordinatePair) -> int:
        row, col = coord_pair
        return row * self.cols + col

    def row_n_iter(self, n: int) -> Iterator[int]:
        return (self._values_store[n, col] for col in range(self.cols))

    def col_n_iter(self, n: int) -> Iterator[int]:
        return (self._values_store[row, n] for row in range(self.rows))

    def transposed(self) -> "Matrix":
        transposed_store = defaultdict(
            int, {(col, row): v for (row, col), v in self._values_store.items()}
        )
        return Matrix(rows=self.cols, cols=self.rows, store=transposed_store)
