import pytest
import Main_Lib

class TestCalculator:

    @pytest.fixture
    def addition(self):
        return 5, 5, '+'

    @pytest.fixture
    def subtraction(self):
        return 5, 5, '-'

    @pytest.fixture
    def multiplication(self):
        return 5, 5, '*'

    @pytest.fixture
    def division(self):
        return 5, 5, '/'

    @pytest.fixture
    def division_without_residue(self):
        return 5, 4, '//'

    @pytest.fixture
    def division_on_zero(self):
        return 5, 0, '/'

    @pytest.fixture
    def division_and_multiplication(self):
        return 4, 5, '/', '*'

    def test_addition(self, addition):
        assert Main_Lib.calculator(*addition) == 10

    def test_subtraction(self, subtraction):
        assert Main_Lib.calculator(*subtraction) == 0

    def test_multiplication(self, multiplication):
        assert Main_Lib.calculator(*multiplication) == 25

    def test_division(self, division):
        assert Main_Lib.calculator(*division) == 1

    def test_division_without_residue(self, division_without_residue):
        assert Main_Lib.calculator(*division_without_residue) == None

    def test_division_on_zero(self, division_on_zero):
        with pytest.raises(ZeroDivisionError):
            Main_Lib.calculator(*division_on_zero)

    def test_division_and_multiplication(self, division_and_multiplication):
        with pytest.raises(TypeError):
            Main_Lib.calculator(*division_and_multiplication)