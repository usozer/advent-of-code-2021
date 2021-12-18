from math import floor, ceil, sqrt
import re

with open("data/day17.txt") as f:
    raw = f.read()

    match = re.search("target area: x=(\d+)..(\d+), y=(-\d+)..(-\d+)", raw)
    x_low, x_high, y_low, y_high = [int(match.group(i)) for i in range(1,5)]

# Part 1
print((-y_low*(-y_low-1))/2)

# Part 2
def calc_x_bound(lower, upper):
    x_lower = (sqrt(8*lower-1) - 1)/2
    x_upper = (sqrt(8*upper-1) - 1)/2

    return ceil(x_lower), floor(x_upper)


def get_velocity(step, lower, upper):
    lower_exact = (lower/step) + (step/2) - (1/2)
    upper_exact = (upper/step) + (step/2) - (1/2)

    lower_bound = ceil(lower_exact)
    upper_bound = floor(upper_exact)

    return list(range(lower_bound, upper_bound+1))

def compile_each(x_lower, x_upper, y_lower, y_upper):
    y = {}

    for i in range(1,1000):
        cur = get_velocity(i, y_lower, y_upper)
        y[i] = cur
    
    y_max = max(y.keys())

    x_bound_low, x_bound_up = calc_x_bound(x_lower, x_upper)

    x = {i:get_velocity(i, x_lower, x_upper) for i in range(1,x_bound_low+1)}
    
    for i in range(x_bound_low+1, y_max+1):
        x[i] = list(range(x_bound_low, x_bound_up+1))

    return(x,y)

def calc_combinations(x_dict, y_dict):
    all_combs = set()
    
    step_max = max(x_dict.keys())

    for i in range(1,step_max+1):

        for x in x_dict[i]:
            for y in y_dict[i]:
                all_combs = all_combs | {(x,y)}

    print(len(all_combs))

calc_combinations(*compile_each(x_low,x_high,y_low,y_high))