import pytest
import Main_Lib

# Тест функции, выдаюшей ряд фибоначи n чисел
class TestFibon:
    # Тестируем программу на коректных данных. Функция возвращает списко элементов.
    def test_on_correct_n(self):
        assert Main_Lib.fibon(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_zero_n(self):
        assert Main_Lib.fibon(0) == None

    def test_one_n(self):
        assert Main_Lib.fibon(1) == [1]

    # Тестируем программу на некоррктных данных. Функция вызывает исключение TypeError.
    def test_on_over_type(self):
        with pytest.raises(TypeError):
            Main_Lib.fibon('10')
