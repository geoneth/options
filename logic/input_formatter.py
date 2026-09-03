import numpy as np
from global_info.config import param_rules, disallow_nan
import math


HEATMAP_SIZE = 8

def calculator(**kwargs):
    return_dict = {}
    for key,value in kwargs.items():
        return_dict[key] = single_value_check(key, value)
    return return_dict

def heatmap(**kwargs):
    return_dict = {}
    first_list = True
    for key, value in kwargs.items():
        if isinstance(value, list):
            # make sure every item in the list follows the rule
            currently_safe = True
            for val in value:
                if not safe(key, val):
                    return_dict[key] = np.nan
                    currently_safe = False
                    break
            # if the list is valid format it to generate required output
            if currently_safe:
                if first_list:
                    return_dict[key] = heatmap_first_list_set_up(value)
                    first_list = False
                else:
                    return_dict[key] = heatmap_second_list_set_up(value)


        else:
            return_dict[key] = single_value_check(key, value)
    return return_dict


def single_value_check(check_using, value_to_check):
    if not safe(check_using, value_to_check):
        return np.nan
    else:
        return np.array(float(value_to_check))

def heatmap_first_list_set_up(items):
    item_list = list_split_manager(items)
    temp = []
    for i in range(HEATMAP_SIZE):
        temp.append(item_list)
    return np.array(temp)

def heatmap_second_list_set_up(items):
    item_list = list_split_manager(items)
    temp = []
    for item in item_list:
        temp.append([item])
    return np.array(temp)



def split_list_for_heatmap(list_lower_bound, list_upper_bound):
    return list(np.linspace(float(list_lower_bound), float(list_upper_bound), num=HEATMAP_SIZE))

def list_split_manager(list_to_check):
    #these heatmap lists will only ever be on len 2 
    #see core info for why

    # this sheuld always be true bc of the way core info is formatted
    # but we introduce the split to keep it going even if the core info dict gets messed up

    # this can be optimized a little by reducing the number of times i convert to a float
    # but it doesnt impact preformance much and i think its easier to read so ill leave it for now
    if float(list_to_check[0]) <= float(list_to_check[1]):
        return split_list_for_heatmap(list_to_check[0], list_to_check[1])
    else:
        return split_list_for_heatmap(list_to_check[1], list_to_check[0])


def safe(dict_key, value):
    #make sure its a float and not None
    #then make sure its not nan or inf since those would pass through
    #then make sure the number follows the rule
    # I could make this 3 more functions but i think its easier to think about when grouped
    # plus its small enough to not matter too too much
    try:
        val = float(value)
    except (ValueError, TypeError):
        return False
    if math.isnan(val) or val == float('inf') or val == float('-inf'):
        return False
    # This is generally bad
    # but im ok with the eval here bc I already checked stuff before it so here it must be a float that works
    # would not work if order is changed
    if not eval(f"{val}{param_rules[dict_key]}"):
        return False
    return True

format_dict = {
        "calculator": calculator,
        "heatmap": heatmap,
        }

def format(viz, **kwargs):
     answer = format_dict[viz](**kwargs)
     return {key: np.round(value, decimals=2) for key, value in answer.items() if not (key in disallow_nan and np.isnan(value))}
