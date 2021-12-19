import functions

import time

def test_min_none():
    try:
        functions.get_min([])
    except ValueError:
        pass

def test_min_single():
    answer = functions.get_min([1])
    assert(answer == 1)

def test_min_general():
    answer = functions.get_min([4, -1, 3, 14])
    assert(answer == -1)


def test_min_first_value():
    answer = functions.get_min([1, 2, 3, 4])
    assert(answer == 1)


def test_min_last_value():
    answer = functions.get_min([4, 3, 2, 1])
    assert(answer == 1)

def test_max_none():
    try:
        functions.get_max([])
    except ValueError:
        pass

def test_max_single():
    answer = functions.get_max([1])
    assert(answer == 1)

def test_max_general():
    answer = functions.get_max([4, -1, 3, 14])
    assert(answer == 14)


def test_max_first_value():
    answer = functions.get_max([1, 2, 3, 4])
    assert(answer == 4)


def test_max_last_value():
    answer = functions.get_max([4, 3, 2, 1])
    assert(answer == 4)


def test_sum_none():
    try:
        functions.get_sum([])
    except ValueError:
        pass

def test_sum_single():
    answer = functions.get_sum([1])
    assert(answer == 1)

def test_sum_general():
    answer = functions.get_sum([4, -1, 3, 14])
    assert(answer == 20)

def test_prod_none():
    try:
        functions.get_prod([])
    except ValueError:
        pass

def test_prod_single():
    answer = functions.get_prod([1])
    assert(answer == 1)

def test_prod_general():
    answer = functions.get_prod([4, -1, 3, 14])
    assert(answer == -168)

def test_prod_zero():
    answer = functions.get_prod([4, -1, 0, 14])
    assert(answer == 0)



def test_min():
    test_min_none()
    test_min_single()
    test_min_general()
    test_min_first_value()
    test_min_last_value()

def test_max():
    test_max_none()
    test_max_single()
    test_max_general()
    test_max_first_value()
    test_max_last_value()

def test_sum():
    test_sum_none()
    test_sum_single()
    test_sum_general()

def test_prod():
    test_prod_none()
    test_prod_single()
    test_prod_general()
    test_prod_zero()

def generate_test_file(path, size):
    with open(path, 'w') as f:
        for i in range(size):
            print(i + 1, file=f)



def test_running_times():
    sizes = [1, 10, 100, 1000, 10000, 100000, 1000* 1000, 10 * 1000 * 1000]
    result = []
    file_name = 'test.txt'
    for size in sizes:
        generate_test_file(file_name, size)
        start = time.time()
        functions.get_values_from_file(file_name)
        end = time.time()
        result.append(end - start)
    return sizes, result

def test_commutativity_sum(first, second):
    return (functions.get_sum([first, second]), functions.get_sum([second, first]))

def test_commutativity_prod(first, second):
    return (functions.get_prod([first, second]), functions.get_prod([second, first]))

def test_commutativity(first, second):
    print(f'Testing commutativity with values: {first}, {second}')
    first_sum, second_sum = test_commutativity_sum(first, second)
    first_prod, second_prod = test_commutativity_prod(first, second)
    print(f'Sum results: {first} + {second} = {first_sum}; {second} + {first} = {second_sum}; absolute difference between answers: {abs(second_sum - first_sum)}')
    print(f'Prod results: {first} * {second} = {first_prod}; {second} * {first} = {second_prod}; absolute difference between answers: {abs(second_prod - first_prod)}')
    

def test():
    test_min()
    test_max()
    test_sum()
    test_prod()
    print("All correctness tests passed.")
    print()
    sizes, running_times = test_running_times()
    for i in range(len(sizes)):
        print(f'Processing file of size {sizes[i]} took {running_times[i]} seconds')
    print()
    test_commutativity(2, 3)
    print()
    test_commutativity(2.123, 1e100)

if __name__ == "__main__":
    test()