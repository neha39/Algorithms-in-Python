# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_value = 0
    index_first_max = -1
    index_second_max = -1
    
    for i in range(n):
        if (index_first_max == -1 or numbers[i] > numbers[index_first_max]):
            index_first_max = i 
            
    for i in range(n):
        if (index_first_max != i and (index_second_max == -1 or numbers[i] > numbers[index_second_max])):
            index_second_max = i
            print
            
    return numbers[index_first_max] * numbers[index_second_max]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

