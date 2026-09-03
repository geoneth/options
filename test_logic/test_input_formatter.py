import sys
sys.path.append("..")
from logic import input_formatter as I
import numpy as np

def test_safe_value_error():
    # here the key plays no role so it can be anything
    # and the value of the string only matters if its a num, nan, or inf
    # however that is tested later
    assert I.safe("stock_price", "cat") == False
    assert I.safe("stock_price", "np.nan") == False
    

def test_safe_type_error():
    # this check should catch if its None
    # yet again key does not matter
    assert I.safe("stock_price", None) == False

def test_safe_nan_inf():
    # then the last non floats it can be are nan inf or -inf
    # therefore we confirm that this works as expected
    # yet again key does not matter
    assert I.safe("stock_price", "nan") == False
    assert I.safe("stock_price", "inf") == False
    assert I.safe("stock_price", "-inf") == False
    

def test_safe_all_eval():
    assert I.safe("stock_price", "-1") == False
    assert I.safe("strike_price", "-1") == False
    assert I.safe("time_to_maturity", "0") == False
    assert I.safe("volatility", "0") == False
    assert I.safe("risk_free_rate", "-1") == False
    assert I.safe("depth", "0") == False
    assert I.safe("steps", "0") == False
    assert I.safe("simulations", "0") == False
    assert I.safe("expected_return", "-1") == False 
    

def test_safe_good_input():
    assert I.safe("stock_price", "0.5") == True
    assert I.safe("strike_price", "0.5") == True
    assert I.safe("time_to_maturity", "0.5") == True
    assert I.safe("volatility", "0.5") == True
    assert I.safe("risk_free_rate", "0.5") == True
    assert I.safe("depth", "1") == True
    assert I.safe("steps", "1") == True
    assert I.safe("simulations", "1") == True
    assert I.safe("expected_return", "0.5") == True

def test_heatmap_first_list_set_up_format():
    assert np.shape(I.heatmap_first_list_set_up([1,8])) == (8, 8)

def test_heatmap_second_list_set_up_format():
    assert np.shape(I.heatmap_second_list_set_up([1,8])) == (8, 1)
