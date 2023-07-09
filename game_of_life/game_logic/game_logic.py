from itertools import product
from random import randint

Grid = list[list[int]]


class GameOfLife:
    """Класс для описания логики игры "Жизнь"."""
    NEIGHBORS_FOR_LIVE: tuple[int] = (2, 3)
    NEIGHBORS_FOR_REBORN: int = 3

    def __init__(self, width: int, height: int) -> None:
        self._width: int = width
        self._height: int = height
        self._grid: Grid = self._create_grid()

    def _create_grid(self) -> Grid:
        """
        Создает игровую сетку, у каждой клетки может быть два состояния: живая(1) или мертвая(0).
    Состояния клеток выбираются случайным образом.
        """

        return [[randint(0, 1) for _ in range(self._width)] for _ in range(self._height)]

    def _count_live_neighbors(self, row: int, column: int) -> int:
        """Вычисляет количество живых соседей."""
        count: int = 0
        neighbor_positions: list[int] = list(product(range(row - 1, row + 2), range(column - 1, column + 2)))
        for i, j in neighbor_positions:
            if (i, j) == (row,  column):
                continue
            if 0 <= i < self._height and 0 <= j < self._width:
                count += self._grid[i][j]
        return count

    def make_step(self) -> None:
        """Совершает игровой ход, в зависимости от количества живых соседей клеток."""
        new_grid: Grid = [[0] * self._width for _ in range(self._height)]
        for i in range(self._height):
            for j in range(self._width):
                live_neighbors = self._count_live_neighbors(i, j)
                if self._grid[i][j] and live_neighbors in self.NEIGHBORS_FOR_LIVE:
                    new_grid[i][j] = 1
                elif live_neighbors == self.NEIGHBORS_FOR_REBORN:
                    new_grid[i][j] = 1
        self._grid = new_grid

    def get_grid_state(self) -> Grid:
        """Выдает состояние сетки."""
        return self._grid

    def load_grid_state(self, unloaded_grid_state: Grid) -> None:
        "Загружает сетку извне."
        self._grid = unloaded_grid_state

    @property
    def is_all_dead(self) -> bool:
        """Проверяет, все ли клетки мертвы."""
        for row in self._grid:
            for cell in row:
                if cell:
                    return False
        return True
