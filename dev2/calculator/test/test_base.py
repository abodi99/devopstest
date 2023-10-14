from calculator.calculator_helper import CalculatorHelper
import pytest

class BaseTest:
    def setup(self):
        self.calc =  CalculatorHelper()

    def teardown(self):
        return self.calc