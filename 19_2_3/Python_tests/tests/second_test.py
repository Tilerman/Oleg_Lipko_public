#import pytest
from Python_tests.app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9
    # тестируем метод умножения
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 3) == 2
    # тестируем метод деления
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 6, 3) == 3
    # тестируем метод вычитания
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 6, 3) == 9
    # тестируем метод суммирования
