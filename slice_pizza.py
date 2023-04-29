# Title:    slice_pizza
# Author:   Eisha Aqeel
# Date:     October 13, 2021.
# Description:
#   The application should prompt the user to enter their
# pizzas diameter in inches. It will then determine the number
# of slices that pizza can be divided into. It will also calculate
# the area of each slice.

# DECLARATIONS
import math
MAX_DIAMETER = 24
SECOND_BIGGEST_DIAMETER = 20
THIRD_BIGGEST_DIAMETER = 16
FORTH_BIGGEST_DIAMETER = 14
FIFTH_BIGGEST_DIAMETER = 12
MIN_DIAMETER = 8
SMALLEST_SLICE_COUNT = 6
SMALL_SLICE_COUNT = 8
MEDIUM_SLICE_COUNT = 10
BIG_SLICE_COUNT = 12
BIGGEST_SLICE_COUNT = 16

# Input:
# Display message: “Please enter the diameter of your pizza, in inches: ”
# Store the user’s input in the variable pizza_diameter
# Try to get integer value for the diameter
try:
    pizza_diameter = int(input("Please enter the diameter of your pizza, "
                         + "in inches: "))
    # creating successful marker
    isvalid = True
    # If try block failed
except ValueError:
    # creating failed marker
    isvalid = False

# if marker is successful
if isvalid:
    if pizza_diameter > 0:
        # Processing:
        number_of_slices = 0
        if pizza_diameter >= MIN_DIAMETER and pizza_diameter <= MAX_DIAMETER:
            if pizza_diameter < FIFTH_BIGGEST_DIAMETER:
                number_of_slices = SMALLEST_SLICE_COUNT
            elif pizza_diameter < FORTH_BIGGEST_DIAMETER:
                number_of_slices = SMALL_SLICE_COUNT
            elif pizza_diameter < THIRD_BIGGEST_DIAMETER:
                number_of_slices = MEDIUM_SLICE_COUNT
            elif pizza_diameter < SECOND_BIGGEST_DIAMETER:
                number_of_slices = BIG_SLICE_COUNT
            else:
                number_of_slices = BIGGEST_SLICE_COUNT
            slice_area = (1 / number_of_slices) * math.pi * (
                          pizza_diameter / 2)**2
            # Output:
            # Display the message, for valid inputs
            print("A " + str(pizza_diameter) + " inch pizza will yield " +
                  str(number_of_slices) + " slices. Each slice will" +
                  " have an area of " + str(round(slice_area, 2)) +
                  " square inches. ")
        else:
            # Output diameter must be in the range of 8 to 24
            print("The pizza must have a diameter in the range of "
                  + str(MIN_DIAMETER) + " inches to " + str(MAX_DIAMETER)
                  + " inches inclusive!")
    else:
        # output age entered must be a positive number (greater than 0)
        print("The diameter must be a positive number!")
else:
    # output diameter entered must be numeric
    print("The diameter entered must be a numeric whole number.")

input('Press Enter to end this application ')
