# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    fib_list = [0, 1]
    
    while True:
        fib_list.append((fib_list[-2] + fib_list[-1]) % 10)
        if fib_list[-2] == 0 and fib_list[-1] == 1:
            temp1 = fib_list[(to % (len(fib_list) - 2)) + 2]
            temp1 = 9 if temp1 == 0 else temp1 - 1
            temp2 = fib_list[((from_ - 1) % (len(fib_list) - 2)) + 2]
            temp2 = 9 if temp2 == 0 else temp2 - 1
            if temp1 < temp2:
                return temp1 - temp2 + 10
            else:
                return temp1 - temp2
            
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))