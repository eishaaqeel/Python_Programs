# Title:    bowling_scores
# Author:   Eisha Aqeel
# Date:     November 26, 2021.
# Description:
#   The application should display the original bowling scores, followed by
# the player average, high score, and low score. It should also ask if the
# user would like to do another round each time the program's about to end.
# The purpose of this is to learn about Arrays.

from statistics import mean

# DECLARATIONS
SCORE_LOWEST = 0
SCORE_HIGHEST = 300
GAMES_UPPERBOUND = 6
game_array = list()
average_score = 0
highest_score = 0
lowest_score = 0
continue_processing = True
output = " "

# Input
# Repeat the run of the program as long as the user wants to continue.
while continue_processing:
    # Iterating up to the 6 games
    for index in range(GAMES_UPPERBOUND):
        # Creating a boolean here to use with a while loop
        success = False
        # Starting the while loop.
        while not success:
            # Prompt the user for their score on each game
            # try
            try:
                user_input = int(input("Please enter the score for Game "
                                       + str(index+1) + ": "))
                # Validate input from the user
                if SCORE_LOWEST <= user_input <= SCORE_HIGHEST:
                    # Store each value in subsequent elements in the array
                    game_array.append(user_input)
                    # Mark the current loop as successful
                    success = True
                # else
                else:
                    # Inform the user that the score must be between 0 & 300
                    print("Score must be between 0 and 300. Please try again.")
            # When try fail
            except ValueError:
                # Inform the user that the score entered must be numerical,
                # whole number only, no decimals
                print("Scores must be numeric, whole numbers only, no "
                      + "decimals. Please try again.")

    # Processing
    # Determine the average of the six scores & store in the relevant variable
    average_score = round(mean(game_array))
    # Determine the highest score out of the six games
    highest_score = max(game_array)
    # Determine the lowest score out of the six games
    lowest_score = min(game_array)

    # Output
    # Display each game score in between dashes
    print("=" * 105)
    for game_num, num in enumerate(game_array):
        output += "Game " + str(game_num+1) + ": " + str(num) + "       "
    print(output.center(105))
    print("=" * 105)

    # Display the players average
    print("Average Score for Bowler: " + str(average_score))
    # Display the highest score of the six games
    print("High Score for Bowler: " + str(highest_score))
    # Display the lowest score of the six games
    print("Low Score for Bowler: " + str(lowest_score))

    # Prompt the user to ask if they would like to process another bowler’s
    # scores for average calculation and high/low determination
    continue_choice = input("\nWould you like to process another set of "
                            + "bowler scores?\nPlease enter \'Y\' to continue "
                            + "or \'N\' to exit: ")
    # Continue until they enter either "yes" or "no".
    while continue_choice:
        # If they enter "yes", don't prompt again, set height and weight back
        # to 0, and we'll start over.
        if continue_choice == 'Y' or continue_choice == 'y':
            continue_choice = ""
            game_array = list()
            output = ""
        # If they enter "no", don't prompt again, set continue_processing
        # to false so the program ends.
        elif continue_choice == 'N' or continue_choice == 'n':
            continue_processing = False
            continue_choice = ""
        # If they enter something that isn't "Y" or "N", prompt them again.
        else:
            continue_choice = input("\nPlease enter 'Y' or 'N'. Would you "
                                    + "like to process another set of bowler "
                                    + "scores? ")
