# Title:    prime_numbers
# Author:   Eisha Aqeel
# Date:     October 31, 2021.
# Description:
#   The application displays all the prime numbers up to a
# limit selected by the user, between 2-70.

import os
import math

# To clear previous outputs in console
os.system('cls')

# DECLARATIONS
START_RANGE = 2
END_RANGE = 70

# Input:
print("*" * 80)
print("PRIME NUMBER FINDER".center(80))
print("*" * 80)

# Creating a boolean to use with a while loop
success = False
while not success:
    # Try prompting the user to enter a limit to the prime numbers they want
    try:
        user_input = int(input("Enter a limit to the prime numbers you "
                               + "want displayed: "))
        # Validate input from the user
        if user_input >= START_RANGE and user_input <= END_RANGE:
            # Mark the current loop as successful
            success = True
        else:
            # Inform the user that the value entered has to be between 2 & 70,
            # and prompt to try again
            print("The value entered must be between " + str(START_RANGE)
                  + " and " + str(END_RANGE) + "! Please try again.")
    # When try fails
    except ValueError:
        # Tell the user that the value entered must be a whole number,
        # and prompt to try again
        print("The value entered must be a whole number! "
              + "Please try again.")

# Processing
prime_numbers = []
for num in range(START_RANGE, user_input + 1):
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

# Output
print("*" * 80)
print("Prime Numbers up to " + str(user_input) + ":")
# print with a space in between each prime number
for prime in prime_numbers:
    print(prime, end=' ')

# Prompt the user to press enter to exit
input('\n\nPress the Enter key to end the program')
