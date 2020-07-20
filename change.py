# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]
    min_change = 0
    
    for coin in coins:
        min_change += m // coin
        m = m % coin
    return min_change

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
