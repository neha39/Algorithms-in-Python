# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    value_by_weight = []
    
    for i in range(len(values)):
        value_by_weight.append((values[i] / weights[i], weights[i], values[i]))
        
    value_by_weight.sort(reverse = True)
    
    i = 0 
    while capacity > 0 and i < len(values):
        if capacity >= value_by_weight[i][1]:
            value += value_by_weight[i][2]
            capacity -= value_by_weight[i][1]
            i += 1
        else:
            value += value_by_weight[i][0] * capacity
            capacity = 0 

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))