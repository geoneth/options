import numpy as np

class Node:
    def __init__(self, stock_price):
        self.up = None
        self.down = None
        self.call = None
        self.put = None
        self.stock_price = stock_price


def calculate(stock_price, strike_price, time_to_maturity, volatility, risk_free_rate, depth=15):
    # this is lazy and should get fixed but its fine for now
    # this whole this is slow bc nodes can share children so it grops at the rate of 2^x 
    # i could also make a way to include upperbounds on the input formatter but this is the only value that needs it
    # therefore imma add it here and in future when this gets updated to be more efficient the problem will be solved
    if depth > 20:
        depth = 15
    delta_t = time_to_maturity/depth
    up_factor = np.exp(volatility * np.sqrt(delta_t))
    down_factor = 1/up_factor
    p_up = (np.exp(risk_free_rate * delta_t) - down_factor)/(up_factor - down_factor)
    p_down = 1 - p_up
    temp_node = Node(stock_price)
    root_node = make_tree(stock_price, temp_node, up_factor, down_factor, depth)
    traverse_tree(strike_price, risk_free_rate, delta_t, root_node, p_up, p_down)
    return {
            "call": root_node.call,
            "put": root_node.put,
            }

def make_tree(price, node, u, d, total_depth, current_depth=0):
    if current_depth > total_depth:
        return None
    node = Node(price)
    node.down = make_tree(price * d, node, u, d, total_depth, current_depth=current_depth + 1)
    node.up = make_tree(price * u, node, u, d, total_depth, current_depth=current_depth + 1)
    return node

def traverse_tree(strike_price, interest_rate, delta_t, node, probability_u, probability_d):
    if node is None:
        return
    traverse_tree(strike_price, interest_rate, delta_t, node.down, probability_u, probability_d)
    traverse_tree(strike_price, interest_rate, delta_t, node.up, probability_u, probability_d)
    if node.up is None and node.down is None:
        node.call = call_exercise_value(strike_price, node)
        node.put = put_exercise_value(strike_price, node)
    else:
        node.call = standard_call_solve(strike_price, interest_rate, delta_t, node, probability_u, probability_d)
        node.put = standard_put_solve(strike_price, interest_rate, delta_t, node, probability_u, probability_d)
    return

def standard_call_solve(strike_price, interest_rate, delta_t, node, Pu, Pd):
    binomial_value = (Pu * node.up.call + Pd * node.down.call) * np.exp(-1*interest_rate*delta_t)
    exercise_value = call_exercise_value(strike_price, node)
    return np.maximum(binomial_value, exercise_value)

def standard_put_solve(strike_price, interest_rate, delta_t, node, Pu, Pd):
    binomial_value = (Pu * node.up.put + Pd * node.down.put) * np.exp(-1*interest_rate*delta_t)
    exercise_value = put_exercise_value(strike_price, node)
    return np.maximum(binomial_value, exercise_value)

def call_exercise_value(strike_price, node):
    return exercise_value_validation(node.stock_price - strike_price)

def put_exercise_value(strike_price, node):
    return exercise_value_validation(strike_price - node.stock_price)

def exercise_value_validation(value):
    return np.maximum(value, 0)

