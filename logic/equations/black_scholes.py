import numpy as np
from scipy.stats import norm 



def calculate(stock_price, strike_price, time_to_maturity, volatility, risk_free_rate):
    d_one = (np.log(stock_price/strike_price) + time_to_maturity * (risk_free_rate + (volatility**2)/2))/(volatility * np.sqrt(time_to_maturity))
    d_two = d_one - volatility*np.sqrt(time_to_maturity)
    call = stock_price * N(d_one) - strike_price * np.exp(-1*risk_free_rate*time_to_maturity) * N(d_two)
    put = strike_price * np.exp(-1 * risk_free_rate * time_to_maturity) * N(-1 * d_two) - stock_price * N(-1 * d_one)

    return {
            "call": call, 
            "put": put
            }




def N(val):
    return norm.cdf(val)
