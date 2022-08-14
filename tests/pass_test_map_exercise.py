from csv import DictReader

import pytest

from exercises.map import MapExercise


class TestMapExercise:
    @pytest.fixture
    def list_of_movies(self) -> list[dict]:
        with open("tests/fixtures/movies.csv", "r") as movies:
            list_of_movies = list(DictReader(movies))
        return list_of_movies

    def test_rating(self, list_of_movies: list[dict]) -> None:
        average_rating = MapExercise.rating(list_of_movies)
        assert round(average_rating, 15) == 6.809410385259628

    def test_chars_count(self, list_of_movies: list[dict]) -> None:
        chars_count = MapExercise.chars_count(list_of_movies, 5)
        assert chars_count == 3850

        chars_count = MapExercise.chars_count(list_of_movies, 8.5)
        assert chars_count == 40

        chars_count = MapExercise.chars_count(list_of_movies, 50)
        assert chars_count == 0
