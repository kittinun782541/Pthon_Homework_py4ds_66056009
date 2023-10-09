import random

def roll_dice(num_of_dice):
    """
    Calculate the total sum of rolling a certain number of dice.

    Parameters:
        num_of_dice (int): The number of dice to roll.

    Returns:
        int: The total sum of the dice rolls.
    """

    # Start the sum total at 0:
    total = 0

    # Run a loop for each die that needs to be rolled:
    for i in range(num_of_dice):
        # Add the amount from one 6-sided dice roll to the total:
        total += random.randint(1, 6)

    # Return the dice roll total:
    return total
#fix to this