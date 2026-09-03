import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

def format(vis_type, input_data, output_data):
    if vis_type == "heatmap":

        formatted_stock_price = format_stock_price(input_data["stock_price"])
        
        formatted_volatility = format_volatility(input_data["volatility"])
        
        formatted_call_output = format_output(output_data["call"])
        formatted_put_output = format_output(output_data["put"])
        
        call_heatmap = make_heatmap("call", formatted_stock_price, formatted_volatility, formatted_call_output)
        put_heatmap = make_heatmap("put", formatted_stock_price, formatted_volatility, formatted_put_output)
        
        return {
                "call": call_heatmap,
                "put": put_heatmap,
                }
    else:
        return {key: np.round(value, decimals=2) for key, value in output_data.items()}


def format_stock_price(data):
    # this needs to be changed from nested arrays to one list 
    # 8x8
    # data should be formatted from smallest to largest no repeats
    return [np.round(val, decimals=2) for val in data[0]]

def format_volatility(data):
    # from nested arrays to one list 
    # 8x1
    # top value first, bottom value last
    return_list = []
    for i in range(len(list(data))-1, -1, -1):
        return_list.append(np.round(data[i][0], decimals=2))
    return return_list
    

def format_output(data):
    # currently formatted as [0][0] being bottom left and [0][n] being top left
    # needs to be formatted so [0][0] on the new list is top left and [0][n] is top right
    # pretty much we take the last index of each list and it becomes its own list then second to last and so on
    # this solution is only valid if stock price is kept as horizontal and volatility is vertical
    return np.round(np.flip(np.array(data), axis=0), decimals=2).tolist()


def make_heatmap(name, bottom_labels, side_labels, data):

    img = BytesIO()
    


    df = pd.DataFrame(data)
    sns.heatmap(
            df,
            xticklabels=bottom_labels,
            yticklabels=side_labels,
            cmap="RdYlGn",
            annot=True,
            cbar=False,
            annot_kws={"size": 7}
            )
    plt.title(f"{name} value (Dollars)")



    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)

    return base64.b64encode(img.getvalue()).decode("utf8")
