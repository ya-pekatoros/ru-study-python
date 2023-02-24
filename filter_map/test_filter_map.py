from .filter_map import FilterMapExercise


def is_not_null_even(x: int) -> tuple[bool, int]:
    if not x or x % 2:
        return False, 0
    return True, x


def square_positive(x: int) -> tuple[bool, int]:
    if x >= 0:
        return True, x * x
    return False, 0


class TestFilterMapExercise:
    def test_filter_map_empty(self) -> None:
        empty = FilterMapExercise.filter_map(is_not_null_even, [])
        assert empty == []

    def test_filter_map_is_not_null_even(self) -> None:
        filtered_list = FilterMapExercise.filter_map(is_not_null_even, [-1, 0, 1, 2, 4])
        assert filtered_list == [2, 4]

    def test_filter_map_square_positive(self) -> None:
        filtered_list = FilterMapExercise.filter_map(square_positive, [-1, 0, 1, 2, 4])
        assert filtered_list == [0, 1, 4, 16]
