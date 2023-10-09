def test_calc_sum(numbers):
        return sum(numbers)

def test_calc_prod(numbers):
    if not numbers:  # If the list is empty, return 1
        return 1
    result = 1
    for number in numbers:
        result *= number
    return result

