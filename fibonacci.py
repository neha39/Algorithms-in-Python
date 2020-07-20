# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    fib_list = [0, 1]
    for i in range (2, n+1):
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list[-1]
        

n = int(input())
print(calc_fib(n))
