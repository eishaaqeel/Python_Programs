# Eisha Aqeel
# September 26, 2021.
# BMI calculator
#
# Requirements:
# create a simple Python application that will calculate the Body Mass Index
# of a person based on the height and weight that the user inputs.

# Input:
# Display message: “Enter height in inches: ”
# Store the user’s input in the variable height_inches
height_inches = float(input('Enter height in inches: '))

# Display message: “Enter weight in pounds: ”
# Store the user’s input in the variable weight_pounds
weight_pounds = float(input('Enter weight in pounds: '))

# Processing:
# MAGIC_NUMBER = 703 as a constant
# calculated_bmi = (weight_pounds / height_inches**2)*703

calculated_bmi = float(weight_pounds / (height_inches ** 2)) * 703

# Output:
# Display the message: “The BMI for a " + str(height_inches) + " inch tall
# person who weighs " + str(weight_pounds) + " lb. is ” followed by
# calculated_bmi as a number with one decimal place.

print("The BMI for a " + str(height_inches) + " inch tall person who weighs "
      + str(weight_pounds) + " lb. is " + str(round(calculated_bmi, 1)))

# Display the message: “Press the Enter key to end this application ”
input('\nPress the Enter key to end this application ')
