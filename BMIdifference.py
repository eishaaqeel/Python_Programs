# Title:    BMI Calculator using loops
# Author:   Eisha Aqeel
# Date:     October 8, 2020.
# Description:
#   The application should prompt the user to enter their height in inches as
# well as their weight in pounds. It will then determine and output the
# difference in their BMI if they lost weight, successively, in increments of
# 5 pounds up to a maximum of 15% of their body weight. Valid heights are in
# the range of 24" to 120", and any weight above 25 lbs is considered valid.
# As BMIs are determined and output, a “category” should is listed with them.

# DECLARATIONS

# Constants representing the minimum and maximum height, for validation.
MINIMUM_HEIGHT = 24
MAXIMUM_HEIGHT = 120
# Constant for the minimum weight, for validation.
MINIMUM_WEIGHT = 25

# Conversion constant for unit conversion
CONVERSION_CONSTANT = 703
# Constants for the weight increment and percentage, used as part of the
# successive weight calculations.
WEIGHT_INCREMENT = 5
MAXIMUM_WEIGHT_PERCENTAGE = 0.15

# Constants for the various BMI ranges
BMI_SEVERELY_UNDERWEIGHT = 16
BMI_UNDERWEIGHT = 18.5
BMI_HEALTHY = 25
BMI_OVERWEIGHT = 30

# Declare variables for the inputs, which assists with validation.
height = 0.0
weight = 0.0

# Declare a variable to indicate whether the user wants to continue or not.
continue_processing = True

# INPUT

# Repeat the run of the program as long as the user wants to continue.
while continue_processing:

    # Validate height.
    # Repeat this until height has been entered and validated.
    while not height:
        try:
            # Prompt the user for height and convert it to a float value.
            height = float(input("Please enter the person's height in"
                           + " inches: "))

            # Check the range of the height.
            if not (MINIMUM_HEIGHT <= height <= MAXIMUM_HEIGHT):
                # Height is invalid. Prompt the user.
                print("Please enter the height between " + str(MINIMUM_HEIGHT)
                      + " and " + str(MAXIMUM_HEIGHT) + " inches.")
                # Set height back to 0 so that the loop will repeat.
                height = 0

        # If the conversion to a float type fails, tell the user.
        except ValueError:
            print("Please enter the height as a numeric value.")

    # Validate weight.
    # Repeat this until weight has been entered and validated.
    while not weight:
        try:
            # Prompt the user for weight and convert it to a float value.
            weight = float(input("Please enter the person's weight in"
                                 + " pounds: "))

            # Check the range of the weight.
            if not (MINIMUM_WEIGHT <= weight):
                # Weight is invalid. Prompt the user.
                print("Please enter a weight of at least " +
                      str(MINIMUM_WEIGHT) + " pounds.")
                # Set Weight back to 0 so that the loop will repeat.
                weight = 0
        # If the conversion to a float type fails, tell the user.
        except ValueError:
            print("Please enter the weight as a numeric value.")

    # PROCESSING

    # Determine te minimum_weight, by subtracting the proportions part
    # of the weight
    minimum_weight = weight - (weight * MAXIMUM_WEIGHT_PERCENTAGE)

    # Repeat until it's gone below 15% of body weight
    while weight >= minimum_weight:
        # Calculate the BMI
        bmi = weight / (height ** 2) * CONVERSION_CONSTANT

        # OUTPUT the height, weight and BMI
        print("The BMI for a " + str(height) + "\" tall person who weighs " +
              str(weight) + " lb. is " + str(round(bmi, 1)), end=", ")
        break

    # Select appropriate category for the BMI and output that
    if bmi >= BMI_OVERWEIGHT:
        weight -= WEIGHT_INCREMENT
    elif bmi >= BMI_UNDERWEIGHT:
        weight -= WEIGHT_INCREMENT
    elif bmi >= BMI_SEVERELY_UNDERWEIGHT:
        weight -= WEIGHT_INCREMENT
    else:
        bmi >= BMI_HEALTHY

    # Decrease the weight by the increment
    weight -= WEIGHT_INCREMENT

    # The remainder of the program is just used to prompt the user to
    # enter values again.
    # Prompt the user to start from the beginning again.
    continue_choice = input("\nWould you like to enter data for another"
                            + "person? (yes/no): ")

    # Continue until they enter either "yes" or "no".
    while continue_choice:
        # If they enter "yes", don't prompt again, set height and weight back
        # to 0, and we'll start over.
        if continue_choice.lower().strip() == "yes":
            continue_choice = ""
            height = 0
            weight = 0
        # If they enter "no", don't prompt again, set continue_processing to
        # false so the program ends.
        elif continue_choice.lower().strip() == "no":
            continue_processing = False
            continue_choice = ""
        # If they enter something that isn't "yes" or "no", prompt them again.
        else:
            continue_choice = input("\nPlease enter 'yes' or 'no'. Would you"
                                    + "like enter data for another person?: ")
