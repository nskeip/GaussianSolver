from collections import defaultdict
from typing import List, Tuple, TypeVar


Numeric = TypeVar("Numeric", int, float)


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self._values_store = defaultdict(lambda: 0)

    def to_list_of_rows(self) -> List[List[Numeric]]:
        return [
            [self._values_store[r, c] for c in range(self.cols)]
            for r in range(self.rows)
        ]

    def __setitem__(self, key: Tuple[int, int], value: Numeric):
        self._values_store[key] = value

    def __str__(self):
        cols_fmt = "\t".join(["{:10f}"] * self.cols)
        return "\n".join(cols_fmt.format(*r).strip() for r in (self.to_list_of_rows()))
