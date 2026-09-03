from global_info.config import core_info

def solve(version, equation, data):
    # see dict
     return core_info[version][equation]["func"](**data) 

