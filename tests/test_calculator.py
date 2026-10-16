import pytest
from src.calculator import Calculator


class TestCalculator:

    def setup_method(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 5) == 15

    def test_add_negative_numbers(self):
        assert self.calc.add(-2, -3) == -5
        assert self.calc.add(-10, 5) == -5

    def test_add_zero(self):
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5

    def test_subtract_positive_numbers(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 5) == 5

    def test_subtract_negative_numbers(self):
        assert self.calc.subtract(-2, -3) == 1
        assert self.calc.subtract(5, -3) == 8

    def test_multiply_positive_numbers(self):
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(10, 5) == 50

    def test_multiply_by_zero(self):
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 5) == 0

    def test_divide_positive_numbers(self):
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            self.calc.divide(5, 0)

    def test_divide_negative_numbers(self):
        assert self.calc.divide(-6, 3) == -2
        assert self.calc.divide(6, -3) == -2

    def test_power_positive_numbers(self):
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25

    def test_power_zero(self):
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(0, 5) == 0

    def test_calculate_add(self):
        assert self.calc.calculate('add', 2, 3) == 5

    def test_calculate_subtract(self):
        assert self.calc.calculate('subtract', 5, 3) == 2

    def test_calculate_multiply(self):
        assert self.calc.calculate('multiply', 2, 3) == 6

    def test_calculate_divide(self):
        assert self.calc.calculate('divide', 6, 3) == 2

    def test_calculate_power(self):
        assert self.calc.calculate('power', 2, 3) == 8

    def test_calculate_invalid_operation(self):
        with pytest.raises(ValueError, match="Неизвестная операция"):
            self.calc.calculate('invalid', 2, 3)

    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 2.5, 5.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        assert self.calc.add(a, b) == expected

    def test_multiple_operations(self):
        result = self.calc.add(2, 3)
        result = self.calc.multiply(result, 2)
        result = self.calc.subtract(result, 1)
        assert result == 9