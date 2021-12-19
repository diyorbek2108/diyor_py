def read_from_file(path):
    with open(path, 'r') as f:
        numbers = list(map(int, f.readline().split()))
    return numbers

def get_min(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty array")
    
    min_value = numbers[0]
    for i in range(1, len(numbers)):
        min_value = min(min_value, numbers[i])
    return min_value

def get_max(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty array")
    
    max_value = numbers[0]
    for i in range(1, len(numbers)):
        max_value = max(max_value, numbers[i])
    return max_value


def get_sum(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty array")
    
    sum_value = 0 
    try:
        for i in range(len(numbers)):
            sum_value += numbers[i] 
    except OverflowError:
        print('Overflow occured during sum')
    finally:
        return sum_value
    


def get_prod(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty array")
    
    prod_value = 1 
    try:
        for i in range(len(numbers)):
            prod_value *= numbers[i] 
    except OverflowError:
        print('Overflow occured during prod')
    finally:
        return prod_value

def get_values_from_file(path):
    numbers = read_from_file(path)
    return [get_min(numbers), get_max(numbers), get_sum(numbers), get_prod(numbers)]

def main():
    min_value, max_value, sum_value, prod_value = get_values_from_file('input.txt')
    print('Min:', min_value)
    print('Max:', max_value)
    print('Sum:', sum_value)
    print('Prod:', prod_value)

if __name__ == "__main__":
    main()