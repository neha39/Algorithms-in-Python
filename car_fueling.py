# python3
import sys


def compute_min_refills(distance, tank, stops):
    
    min_fills = 0
    current_fill = 0
    stops = [0] + stops + [distance]
    while current_fill < (len(stops) - 1):
        
        last_fill = current_fill
        
        while current_fill < (len(stops) - 1) and (stops[current_fill + 1] - stops[last_fill]) <= tank :
            current_fill += 1 
        if current_fill == last_fill:
            return -1
        if current_fill < (len(stops) - 1):
            min_fills += 1 
    
    return min_fills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
