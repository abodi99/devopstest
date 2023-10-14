from test_base import BaseTest
import pytest
import json

from calculator.calculator_helper import CalculatorHelper
from calculator_api.configuration import Configuration
from calculator_api.api_client import ApiClient
from calculator_api.models.calculation import Calculation
from calculator_api.models.response import Response
from calculator_api.api.calculator_api import CalculatorApi



class TestCalculater(BaseTest):
    def test_add(self):
        result = self.calc.add(5, 3)
        assert result == 8

    def test_subtract(self):
        result = self.calc.subtract(5, 3)
        assert result == 2

    def test_multiply(self):
        result = self.calc.multiply(5, 3)
        assert result == 15

    def test_divide(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    @pytest.mark.parametrize("a, b, expected_result", [
    (3, 3, 6),
    #(3, -3, 0),
    #(0, 0, 0),  # Additional test case
    #(-5, 5, 0),  # Additional test case
    #(10, 5, 15),  # Additional test case
    ])

    def test_addMult(self, a, b, expected_result):
        result = self.calc.add(a,b)
        assert result == expected_result

    def test_api(self):
        cfg = Configuration()
        cfg.host = "http://localhost:5000"
        client = ApiClient(cfg)
        api = CalculatorApi(client)
        res = api.operations_add_subtract_multiply_divide(Calculation(operation="add", operand1=3,operand2=3))
        result_value = res.result 
        float_result_value = float(result_value)

        assert float_result_value==6      

