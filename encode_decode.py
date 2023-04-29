# Title:    encode_decode
# Author:   Eisha Aqeel
# Date:     November 28, 2021.
# Description:
#   This program allows a user to encode or decode a piece of text.
#   It will convert the users input from English letters to the
#   Al Bhed language from Final Fantasy X or vice versa.

# Declarations:
continue_processing = True
ENCODE = 1
DECODE = 2
EXIT = 3
# define english alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# define Al Bhed alphabet
al_bhed = "YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow"

# Input
# Repeat the run of the program as long as the user wants to continue.
while continue_processing:
    # Creating a boolean here to use with a while loop
    success = False
    # Starting the while loop for choices
    while not success:
        # Prompt the user for their choice
        print("1 = Encode text")
        print("2 = Decode text")
        print("3 = Exit program")
        try:
            user_input = int(input("Please enter an option of 1, 2 or 3: "))
            # Validate input from the user
            if user_input <= EXIT:
                # Mark as successful
                success = True
            else:
                print("Please select a valid option between 1 and 3.")
        # When try fail
        except ValueError:
            print("Please select a valid option between 1 and 3.")
    # Processing
    if user_input == ENCODE:
        # Get the message to be encoded from the user
        message = input("Enter the text you want to encode: ")
        encrypted_string = ""
        # Iterate through each character in the message
        for letter_index in range(len(message)):
            match_found = False
            # Check if the character is in the English alphabet
            for alphabet_index in range(len(alphabet)):
                # If it is, replace it with the corresponding Al Bhed character
                if message[letter_index] == alphabet[alphabet_index]:
                    encrypted_string += al_bhed[alphabet_index]
                    match_found = True
            # If the character is not in the English alphabet, leave it as is
            if not match_found:
                encrypted_string += message[letter_index]
        encoded_text = encrypted_string
    # else if the user choose to decode,
    elif user_input == DECODE:
        # Get the message to be decoded from the user
        message = input("Enter the text you want to decode: ")
        decrypted_string = ""
        # Iterate through each character in the message
        for letter_index in range(len(message)):
            match_found = False
            # Check if the character is in the Al Bhed alphabet
            for al_bhed_index in range(len(al_bhed)):
                # If it is,
                if message[letter_index] == al_bhed[al_bhed_index]:
                    # replace it with the corresponding English character
                    decrypted_string += alphabet[al_bhed_index]
                    match_found = True
            # If the character is not in the Al Bhed alphabet, leave it as is
            if not match_found:
                decrypted_string += message[letter_index]
        decoded_text = decrypted_string
    # else if the user chooses to Exit
    elif user_input == EXIT:
        continue_processing = False
        break
    else:
        # Inform the user if they input an invalid option
        print("Invalid choice!")
        continue

    # Output
    # Print the encoded or decoded
    if user_input == ENCODE:
        print(f"The encoded text is: {encoded_text}")
    elif user_input == DECODE:
        print(f"The decoded text is: {decoded_text}")
    else:
        continue_processing = False
        break
