import numpy as np

def calculate(stock_price, strike_price, time_to_maturity, volatility, risk_free_rate, expected_return, steps=10, simulations=15):
    call_value_list = []
    put_value_list = []
    DELTA_T = time_to_maturity/steps
    # for every simulation simulate a path the option can take
    for _ in range(int(simulations)):
        steps_list = [stock_price]
        for i in range(1, int(steps)):
            random = np.random.normal()
            next = steps_list[i-1] * np.exp((expected_return - ((volatility*volatility)/2))*DELTA_T + (volatility * np.sqrt(DELTA_T))* random)
            steps_list.append(next)
        # then for each of those paths price the call and put
        # here we are pricing an asian option
        steps_bar = np.average(steps_list, axis=0)

        call_value_list.append(get_call_value(steps_bar, strike_price))
        put_value_list.append(get_put_value(steps_bar, strike_price))
    # then average the values
    call_bar = np.average(call_value_list, axis=0)
    put_bar = np.average(put_value_list, axis=0)
    #finally discount them to account for time
    real_call = discount(call_bar, risk_free_rate, time_to_maturity)
    real_put = discount(put_bar, risk_free_rate, time_to_maturity)

    return {
            "call": real_call,
            "put": real_put,
            }






def get_call_value(a, x):
    return np.maximum(a - x, 0)

def get_put_value(a, x):
    return np.maximum(x - a, 0)

def discount(value, r, t):
    return value * np.exp(-1 * r * t)
