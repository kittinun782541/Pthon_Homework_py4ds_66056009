def get_smallest(numbers):
    """
    Get the smallest number from a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int or None: The smallest number from the list. If the list is empty, returns None.
    """
    # If the numbers list is empty, return None:
    if len(numbers) == 0:
        return None

    # Create a variable that tracks the smallest value so far, and start
    # it off a the first value in the list:
    smallest = numbers[0]

    # Loop over each number in the numbers list:
    for number in numbers:
        # If the number is smaller than the current smallest value, make
        # it the new smallest value:
        if number < smallest:
            smallest = number

    # Return the smallest value found:
    return smallest
 # FIX to this problem