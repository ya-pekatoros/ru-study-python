from exercises.filter_map import FilterMapExercise


class TestFilterMapExercise:
    def test_filter_map(self) -> None:
        def is_odd(x: int) -> tuple[bool, int]:
            if not x or x % 2:
                return False, 0
            return True, x

        empty = FilterMapExercise.filter_map(is_odd, [])
        assert not empty
        assert isinstance(empty, list)

        filtered_list = FilterMapExercise.filter_map(is_odd, [-1, 0, 1, 2, 4])
        assert filtered_list == [2, 4]
