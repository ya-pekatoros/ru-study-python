class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        output_list = []
        max_elem = 0

        for elem in input_list:
            if elem > max_elem:
                max_elem = elem

        for elem in input_list:
            if elem > 0 and elem != max_elem:
                output_list.append(max_elem)
            else:
                output_list.append(elem)

        return output_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        pass
