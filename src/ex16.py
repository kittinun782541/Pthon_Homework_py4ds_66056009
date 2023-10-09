"""
Exercise 16
"""


def mode(input):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    input_len = len(input)
    count = 0
    if input_len == 0:
        return None
    max_count = 0
    element_having_max_freq = 0
    for i in range(0, input_len):
        count = 0
        for j in range(0, input_len):
            if input[i] == input[j]:
                count += 1
        if count > max_count:
            max_count = count
            element_having_max_freq = input[i]

    return element_having_max_freq
#Fix to this