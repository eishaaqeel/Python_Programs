###############################################################################
# Programmers:  Eisha A. & Samson C.
# Program name: Midterm Grades Calculator
# Date:         Nov 19, 2021
# Purpose:      Calculates a Student's midterm grade.
###############################################################################
# Output:
# A midterm grade, as a real number between 0 and 100
# Also output the user's average % on each evaluation category:
# Class Exercises, Pre-Class Activities, Lab, and Academic Integrity Workshop
# as a real number between 0 and 100
# Input:
# Grades on each evaluation, as a real number between 0 and 100 inclusively.
# Process:
# There are four evaluation types: CE, PCA, Lab and AIW.
# Each of these are worth different amounts.
# There are 6 CEs worth 2.5% each, a total weight of 15.
# There are 4 PCAs worth 2% each, a total weight of 8.
# There are 2 Labs worth 8% each, a total weight of 16.
# There is 1 AIW, worth a total weight of 3.
# Total weight is 42
# The numbers of each of these evaluations and their total value will be
# declared as constants.
# Declare an array for each of these evaluation types with elements equal to
# the constant representing the number of evaluations.
# Determine the value of each evaluation in each category by dividing the %
# value by the number of evaluations in that category.
# imports
from statistics import mean

# ***Declarations:
# Declare constants for the number of CEs (6), PCA (4), Labs (2), and AIW (1).
CLASS_EXERCISES_UPPERBOUND = 6
PRE_CLASS_ASSIGNMENTS_UPPERBOUND = 4
LABS_UPPERBOUND = 2
ACADEMIC_INTEGRITY_WORKSHOP_UPPERBOUND = 1
# Declare constants for the overall category maximum values: CE (0.15), PCA
# (0.08), Lab (0.16), and AIW (0.03).
CLASS_EXERCISES_WORTH = 0.15
PRE_CLASS_ASSIGNMENTS_WORTH = 0.08
LABS_WORTH = 0.16
ACADEMIC_INTEG_WS_WORTH = 0.03
# Declare an array for each of these evaluation types.
class_exer_arr = list()
pre_class_assignment_array = list()
labs_array = list()
academic_integrity_workshop_array = list()
# Declare a variable for the average grade in each evaluation category.
average_class_exercises = 0.0
average_pre_class_assignment = 0.0
average_labs = 0.0
average_academic_integrity_workshop = 0.0
total_grade = 0.0

# ***Input:
# Iterating up to the total number of CEs...
for index in range(CLASS_EXERCISES_UPPERBOUND):
    # Starting hte while loop.
    while True:
        # Prompt the user for their grade on each CE as a real
        # number out of 100
        try:
            user_input = float(input("Please enter the grade you received out "
                                     + "of 100 for Class Exercise " +
                                     str(index + 1) + ": "))
            # Validate input from the user - re-prompt as needed
            if 0 <= user_input <= 100:
                # Store each value in subsequent elements in the array for
                # CE grades
                class_exer_arr.append(user_input)
                break
            else:
                # Inform the user that the grade entered must be between
                # 0 and 100.
                print("The grade entered must be between 0 and 100, please "
                      + "try again")
        except ValueError:
            # Inform the user that the grade entered must be numerical
            print("The grade entered must be numerical, please try again")

# Iterating up to the total number of PCA...
for index in range(PRE_CLASS_ASSIGNMENTS_UPPERBOUND):
    # Starting the while loop.
    while True:
        # Prompt the user for their grade on each PCA as a real
        # number out of 100
        try:
            user_input = float(input("Please enter the grade you received out "
                                     + "of 100 for Pre Class Assignment "
                                     + str(index + 1) + ": "))
            # Validate input from the user - re-prompt as needed
            if 0 <= user_input <= 100:
                # Store each value in subsequent elements in the array for
                # PCA grades
                pre_class_assignment_array.append(user_input)
                break
            else:
                # Inform the user that the grade entered must be between
                # 0 and 100.
                print("The grade entered must be between 0 and 100, please "
                      + "try again")
        except ValueError:
            # Inform the user that the grade entered must be numerical
            print("The grade entered must be numerical, please try again")

# Iterating up to the total number of Labs...
for index in range(LABS_UPPERBOUND):
    # Starting hte while loop.
    while True:
        # Prompt the user for their grade on each Lab as a real number
        # out of 100
        try:
            user_input = float(input("Please enter the grade you received out "
                                     + "of 100 for Lab "
                                     + str(index + 1) + ": "))
            # Validate input from the user - re-prompt as needed
            if 0 <= user_input <= 100:
                # Store each value in subsequent elements in the array
                # for Lab grades
                labs_array.append(user_input)
                break
            else:
                # Inform the user that the grade entered must be between
                # 0 and 100.
                print("The grade entered must be between 0 and 100, please " +
                      "try again")
        except ValueError:
            # Inform the user that the grade entered must be numerical
            print("The grade entered must be numerical, please try again")

# Iterating up to the total number of AIW...
for index in range(ACADEMIC_INTEGRITY_WORKSHOP_UPPERBOUND):
    # Starting hte while loop.
    while True:
        # Prompt the user for their grade on each AIW as a real number out
        # of 100
        try:
            user_input = float(input("Please enter the grade you received out "
                                     + "of 100 for Academic Integrity "
                                     + "Workshop " + str(index + 1) + ": "))
            # Validate input from the user - re-prompt as needed
            if 0 <= user_input <= 100:
                # Store each value in subsequent elements in the array for
                # AIW grades
                academic_integrity_workshop_array.append(user_input)
                break
            else:
                # Inform the user that the grade entered must be between
                # 0 and 100.
                print("The grade entered must be between 0 and 100, please "
                      + "try again")
        except ValueError:
            # Inform the user that the grade entered must be numerical
            print("The grade entered must be numerical, please try again")

# *** Processing:
# Determine the average of the CE array, store this in the relevant variable
# using built-in functions
average_class_exercises = sum(class_exer_arr) / len(class_exer_arr)
# Determine the average of the PCA array, store this in the relevant variable,
# using built-in functions
average_pre_class_assignment = sum(pre_class_assignment_array) / len(
    pre_class_assignment_array)
# note, sum() basically does what line [172,174] is doing but have it in
# a function.
# Determine the average of the Lab array, store this in the relevant variable
# using built-in functions
average_labs = sum(labs_array) / len(labs_array)
# Determine the average of the AIW array, store this in the relevant variable
# by importing mean from Statistics library
average_academic_integrity_workshop = mean(academic_integrity_workshop_array)

# Determine the total grade overall:
# Total grade overall: add the average of the CE array multiplied by the weight
# of the CE grades (0.15)
total_grade += average_class_exercises * CLASS_EXERCISES_WORTH

# Total grade overall: add the average of the PCA array multiplied by the
# weight of the PCA grades (0.08)
total_grade += average_pre_class_assignment * PRE_CLASS_ASSIGNMENTS_WORTH

# Total grade overall: add the average of the Lab array multiplied by the
# weight of the Lab grades (0.16)
total_grade += average_labs * LABS_WORTH

# Total grade overall: add the average of the AIW array multiplied by
# the weight of the AIW grades (0.03)
total_grade += average_academic_integrity_workshop * ACADEMIC_INTEG_WS_WORTH

# Since the grade is only out of a portion of the course, we must now get a
# percentage by dividing the user's raw score from the max obtainable.
total_grade = total_grade / (CLASS_EXERCISES_WORTH +
                             PRE_CLASS_ASSIGNMENTS_WORTH + LABS_WORTH +
                             ACADEMIC_INTEG_WS_WORTH)

# *** Output:
# Just printing out an empty line, a \n would also do this, but as an example
print("")
# Output the average of the CE array, with an appropriate identifier
print("Average of your Class Exercises is: " + "{:.2f}".format(round(
    average_class_exercises, 2)))
# Output the average of the PCA array, with an appropriate identifier
print("Average of your Pre Class Assignment is: " + "{:.2f}".format(round(
    average_pre_class_assignment, 2)))
# Output the average of the Lab array, with an appropriate identifier
print("Average of your Lab is: " + "{:.2f}".format(round(average_labs, 2)))
# Output the average of the AIW array, with an appropriate identifier
print("Average of your Academic Integrity is: " + "{:.2f}".format(round(
    average_academic_integrity_workshop, 2)))

# Output the (total grade overall / summation of the weight of all category
# maximum values), with an appropriate identifier.
print("Your Total grade is: " + "{:.2f}".format(round(total_grade, 2)))

# Prompt the user to press enter to exit
input("\nPress Enter to exit program.")
