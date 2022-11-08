import pytest
import Main_Lib

# Тест функции, которая сортирует спсисок методом "Пузырек", и возвращает его копию
class TestIsOrdered:
    # Функция возвращает данные для выполнения теста - упорядоченный от мин к макс список
    @pytest.fixture
    def ordered_example(self):
        return [1, 2, 3, 4, 5]

    # Функция возвращает данные для выполнения теста - неупорядоченный список
    @pytest.fixture
    def unordered_example(self):
        return [5, 3, 1, 2, 4]

    # Функция возвращает данные для выполнения теста - массив равных по величине значений
    @pytest.fixture
    def equal_example(self):
        return [1, 1, 1, 1, 1]

    # Функция возвращает данные для выполнения теста - неупорядоченный список c переменой str
    @pytest.fixture
    def type_error_list(self):
        return [5, 3, 1, 2, 4, '5']

    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_ordered(self, ordered_example):
        assert Main_Lib.sorted_bubble(ordered_example) == [1, 2, 3, 4, 5]

    # Тест функции на неупорядоченных значениях
    def test_on_unordered(self, unordered_example):
        assert Main_Lib.sorted_bubble(unordered_example) == [1, 2, 3, 4, 5]

    # Тест функции на равных по величине значениях
    def test_on_equal(self, equal_example):
        assert Main_Lib.sorted_bubble(equal_example) == [1, 1, 1, 1, 1]

    # Тестируем программу на некоррктных данных. Функция вызывает исключение TypeError.
    def test_on_over_type(self, type_error_list):
        with pytest.raises(TypeError):
            Main_Lib.sorted_bubble(type_error_list)