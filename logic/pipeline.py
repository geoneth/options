from logic import equation_manager as eq_man
from logic import input_formatter as formatter_I
from logic import output_formatter as formatter_O
import numpy as np



def run(version, equation, viz, **kwargs):
    clean_data = formatter_I.format(
            viz,
            **kwargs
            )
    solution = eq_man.solve(version, equation, clean_data)
    return formatter_O.format(viz, clean_data, solution)

