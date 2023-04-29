# Author:   Eisha Aqeel
# Date:     November 30, 2021.
# Description:
#   This is Python code intended to be used with tkinter to
#   enable the functionality for a form designed to take a
#   length and a width from the user, validate those values, then
#   calculate and display both the perimeter and the area of a rectangle.
#   Functionality to clear all fields and exit the application is also
#   available via buttons.

# tkinter is imported to create the GUI.
from tkinter import *
from tkinter.tix import *
# sys is imported for easy exit functionality.
import sys


# Define functions
# Function to perform the validation and calculation.
def calculate_rectangle(_event=None):
    # Input.
    # Validate the input.
    try:
        # Is the input a number?
        valid_length = float(text_length_input.get())
        valid_width = float(text_width_input.get())

        # Is the input a positive number?
        if valid_length > 0 and valid_width > 0:

            # Processing.
            # Calculate the perimeter and area.
            perimeter = valid_length * 2 + valid_width * 2
            area = valid_length * valid_width
            # Output the perimeter and area.
            label_perimeter_output.configure(text=perimeter)
            label_area_output.configure(text=area)
            label_status.configure(text="Calculation successful!")
        # If the input is not positive, display an error message.
        else:
            label_status.configure(text="ERROR: Length and width must both be "
                                   + "positive.")
    # If the input is not a number, display an error message.
    except ValueError:
        label_status.configure(text="ERROR: Length and width must both be "
                               + "numeric.")


# Function to clear all fields; window returns to its default state.
def clear_window(_event=None):
    # Set all input and output fields to be blank.
    label_area_output.configure(text="")
    label_perimeter_output.configure(text="")
    text_length_input.delete(0, END)
    text_width_input.delete(0, END)
    label_status.configure(text="All fields cleared.")
    # Put the focus back on the first input control for fast data entry.
    text_length_input.focus()


# Function to exit the application.
def close_window(_event=None):
    sys.exit()


# Create a window as a tk object.
window = Tk()
window.geometry("640x320")
window.minsize(width=600, height=300)
window.title("Space Eaters")

tooltip = Balloon(window)

# Row 0 controls
# Prompting label for the input length.
# Text entry for the input length.
label_length_prompt = Label(text="Length:")
label_length_prompt.grid(row=0, column=0)
text_length_input = Entry()
text_length_input.grid(row=0, column=1)

# Row 1 controls
# Prompting label for the input width.
# Text entry for the input length.
label_width_prompt = Label(text="Width:")
label_width_prompt.grid(row=1, column=0)
text_width_input = Entry()
text_width_input.grid(row=1, column=1)

# Row 2 controls
# Output label for the area output
text_area_input = Label(text="Area:")
text_area_input.grid(row=2, column=0)
label_area_output = Label(width=20, bd=2, relief=SUNKEN)
label_area_output.grid(row=2, column=1)

# Row 3 controls
# Output label for the perimeter output
text_perimeter_input = Label(text="Perimeter:")
text_perimeter_input.grid(row=3, column=0)
label_perimeter_output = Label(width=20, bd=2, relief=SUNKEN)
label_perimeter_output.grid(row=3, column=1)

# Row 4 controls
# Calculate button
button_calculate = Button(text="Calculate", width=15,
                          command=calculate_rectangle)
button_calculate.grid(row=4, column=0, padx=5, pady=5)
tooltip.bind_widget(button_calculate, msg="Click to calculate the area &"
                    + "perimeter")
# Clear button
button_clear = Button(text="Clear", width=15, command=clear_window)
button_clear.grid(row=4, column=1, padx=5, pady=5)
tooltip.bind_widget(button_clear, msg="Click to clear all fields")
# Exit button
button_exit = Button(text="Exit", width=15, command=close_window)
button_exit.grid(row=4, column=2, padx=5, pady=5)
tooltip.bind_widget(button_exit, msg="Click to exit")

# Row 5 control
# This label acts as a status bar in case hover text or some other form of
# messaging is useful.
label_status = Label(window, width=100, borderwidth=1, relief=SOLID)
tooltip.bind_widget(label_status, msg="Displays status and error messages")
label_status.grid(row=5, columnspan=3, sticky=S)

# Add hotkey support for the three main buttons.
window.bind("<Alt-c>", calculate_rectangle)
window.bind("<Alt-l>", clear_window)
window.bind("<Alt-x>", close_window)

# Launch the window.
window.mainloop()
