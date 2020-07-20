# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
    
def fibonacci_sum_squares(n):
    if n <= 1:
        return n 
    
    fib_list = [0, 1]
    
    while True:
        fib_list.append((fib_list[-2] + fib_list[-1]) % 10)
        if fib_list[-2] == 0 and fib_list[-1] == 1:
            temp1 = fib_list[(n % (len(fib_list) - 2))]
            temp2 = fib_list[(n % (len(fib_list) - 2)) - 1]
            return  (temp1 * (temp1 + temp2)) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
