# Uses python3
import sys
"""
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
"""

def get_fibonacci_huge(n, m):
    fib_list = [0, 1]
    while True:
        fib_list.append((fib_list[-2] + fib_list[-1]) % m) 
        if fib_list[-2] == 0 and fib_list[-1] == 1:
            return fib_list[n % (len(fib_list) - 2)]
# """
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))