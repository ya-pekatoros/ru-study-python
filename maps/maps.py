from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating(movie: dict) -> Union[float, None]:
            if len(movie["country"].split(",")) > 1:
                if movie["rating_kinopoisk"]:
                    return float(movie["rating_kinopoisk"])
            return None

        list_of_ratings = list(
            filter(lambda rate: True if rate else False, map(get_rating, list_of_movies))
        )
        return sum(list_of_ratings) / len(list_of_ratings)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def get_letters_number(movie: dict) -> int:
            count = 0
            for letter in movie["name"]:
                if letter == "и":
                    count += 1
            return count

        movies_rated = filter(
            lambda movie: float(movie["rating_kinopoisk"]) >= rating
            if movie["rating_kinopoisk"]
            else False,
            list_of_movies,
        )
        return sum(list(map(get_letters_number, movies_rated)))
