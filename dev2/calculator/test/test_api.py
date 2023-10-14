import pytest
import json
import requests


from calculator.calculator_helper import CalculatorHelper
from calculator_api.configuration import Configuration
from calculator_api.api_client import ApiClient
from calculator_api.models.calculation import Calculation
from calculator_api.models.response import Response
from calculator_api.api.calculator_api import CalculatorApi

def callAPIwithOp(operator, operand1, operand2):
        cfg = Configuration()
        cfg.host = "http://localhost:5000"
        client = ApiClient(cfg)
        api = CalculatorApi(client)
        res = api.operations_add_subtract_multiply_divide(Calculation(operation=operator, operand1=operand1, operand2=operand2))
        result_value = res.result 
        float_result_value = float(result_value)

        return float_result_value

  

def test_addition():
    assert callAPIwithOp("add", 3, 3) == 6


@pytest.mark.parametrize("operand1, operand2, expected_result", [
(3, 3, 6),
(3, -3, 0),
(0, 0, 0),  
(-5, 5, 0),  
(10, 5, 15),  
])

def test_add( operand1, operand2, expected_result):
    base_url = "http://127.0.0.1:5000"
    endpoint = "/calculator/"  # The endpoint you provided
    url = base_url + endpoint

    payload = {
        "operation": "add",
        "operand1": operand1,
        "operand2": operand2
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 200, "Response status code is not 200 (OK)"

    response_data = response.json()
    assert response_data["result"] == expected_result

    
