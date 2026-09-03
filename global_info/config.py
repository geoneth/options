from logic.equations import black_scholes, binomial, monte_carlo



all_viz_types = ["calculator", "heatmap"]

"""
type: {
        method: {
            dispaly name: name,
            params: [param list],
            func: function,
            route to: location
            available viz types: {
                option: None if no change,
                option_two: {
                    original param: [split to new params],
                    }
                }
            }
        }

"""
core_info = {
        "European": {
            "black_scholes": {
                "display_name": "Black-Scholes",
                "params": [
                    "stock_price",
                    "strike_price",
                    "time_to_maturity",
                    "volatility",
                    "risk_free_rate",
                    ],
                "func": black_scholes.calculate,
                "route_to": "/Calculate",
                "available_viz_types": {
                    "calculator": [None],
                    "heatmap": {
                        "stock_price": ["stock_price_lower_bound", "stock_price_upper_bound"],
                        "volatility": ["volatility_lower_bound", "volatility_upper_bound"],
                        }
                    },
                },#bs close
            },#eu close
        "American": {
            "binomial": {
                "display_name": "Binomial",
                "params": [
                    "stock_price",
                    "strike_price",
                    "time_to_maturity",
                    "volatility",
                    "risk_free_rate",
                    "depth",
                    ],
                "func": binomial.calculate,
                "route_to": "/Calculate",
                "available_viz_types": {
                    "calculator": [None],
                    "heatmap": {
                        "stock_price": ["stock_price_lower_bound", "stock_price_upper_bound"],
                        "volatility": ["volatility_lower_bound", "volatility_upper_bound"],
                        }
                    }, 
                }
            },
        "Asian": {
            "monte_carlo": {
                "display_name": "Monte Carlo",
                "params": [
                    "stock_price",
                    "strike_price",
                    "time_to_maturity",
                    "volatility",
                    "risk_free_rate",
                    "expected_return",
                    "steps",
                    "simulations",
                    ],
                "func": monte_carlo.calculate,
                "route_to": "/Calculate",
                "available_viz_types": {
                    "calculator": [None],
                    "heatmap": {
                        "stock_price": ["stock_price_lower_bound", "stock_price_upper_bound"],
                        "volatility": ["volatility_lower_bound", "volatility_upper_bound"],
                        }
                    },
                }
            },




        } #dict close


disallow_nan = ["depth", "steps", "simulations"]


param_rules = {
    #all param rules go here
    "stock_price": ">=0",
    "strike_price": ">=0",
    "time_to_maturity": ">0",
    "volatility": ">0",
    "risk_free_rate": ">=0",
    "depth": ">=1",
    "steps": ">=1",
    "simulations": ">=1",
    "expected_return": ">=0",
    }
