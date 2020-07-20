# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    if n <= 1:
        return n
        
    fib_list = [0, 1]
    
    while True:
        fib_list.append((fib_list[-2] + fib_list[-1]) % 10)
        if fib_list[-2] == 0 and fib_list[-1] == 1:
            temp = fib_list[(n % (len(fib_list) - 2)) + 2]
            if temp == 0:
                return 9
            else:
                return temp - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
