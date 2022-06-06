import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 5) == 9

    def test_substraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 9, 5) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 12, 3) == 4