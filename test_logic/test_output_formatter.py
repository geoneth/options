import sys
sys.path.append("..")
from logic import output_formatter as O

def test_format_output():
    assert O.format_output([[1,2,3],[4,5,6],[7,8,9]]) == [[3,6,9],[2,5,8],[1,4,7]]
