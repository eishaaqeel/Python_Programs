# Title:    temperature_converter_GUI
# Author:   Eisha Aqeel
# Date:     December 12, 2021.
# Description:
#   This program uses tkinter to create a graphical user interface window that
# accepts a temperature as either Celsius or Fahrenheit and converts that
# temperature to the other scale.

from tkinter import *
from tkinter.tix import *
import sys


# Define functions
# Function to perform the validation and calculation.
def calculate(_event=None):
    # Input.
    # Validate the input.
    try:
        # Is the input a number?
        valid_temperature = float(entry_temperature.get())
        # Processing.
        # If Celsius is selected
        if radio_button_option.get() == 1:
            # Convert from Celsius to Fahrenheit
            fahrenheit = (9.0/5.0 * valid_temperature) + 32
            # output
            output.configure(text=f"{fahrenheit:.1f}")
            label_status.configure(text=f"{valid_temperature:.1f} degrees " +
                                   "Celsius converts to " +
                                   f"{fahrenheit:.1f} degrees Fahrenheit.")
        else:
            # Convert from Fahrenheit to Celsius
            celsius = (valid_temperature - 32) * 5.0/9.0
            output.configure(text=f"{celsius:.1f}")
            label_status.configure(text=f"{valid_temperature:.1f} degrees " +
                                   "Fahrenheit converts to " +
                                   f"{celsius:.1f} degrees Celsius.")
    # If the input is not a number, display an error message.
    except ValueError:
        entry_temperature.delete(0, END)
        label_status.configure(text="ERROR: Please enter a numeric "
                                    + "temperature to convert.")


# Create a window as a tk object.
window = Tk()
window.geometry("600x300")
window.title("Temperature Converter")

# Create a balloon object for tooltips
tooltip = Balloon(window)

# Define radio_button_option
radio_button_option = IntVar()


# Function to clear all fields
def clear(_event=None):
    # Set all input and output fields to be blank.
    output.configure(text="")
    entry_temperature.delete(0, END)
    label_status.configure(text="All fields cleared.")
    # Put the focus back on the first input control for fast data entry.
    entry_temperature.focus()
    # Select the default button
    radio_button_option.set(1)


# Function to exit the application.
def close_window(_event=None):
    sys.exit()


# radio buttons widgets
radio_button_celsius = Radiobutton(window, text="°C",
                                   variable=radio_button_option, value=1)

radio_button_fahrenheit = Radiobutton(window, text="°F",
                                      variable=radio_button_option, value=2)

# Row 0 controls
label_temperature = Label(text="Temperature:")
label_temperature.grid(row=0, column=0, padx=5, pady=5, sticky=E)
entry_temperature = Entry()
entry_temperature.grid(row=0, column=1, sticky=W)
tooltip.bind_widget(entry_temperature, msg="Enter the temperature")

radio_button_celsius.grid(row=0, column=2, padx=5, pady=5, sticky=W)
radio_button_fahrenheit.grid(row=0, column=3, sticky=W, padx=5, pady=5)
# set default selection to 1 (Celsius)
radio_button_option.set(1)

# Row 1 controls
label_result = Label(text="Result:")
label_result.grid(row=1, column=0, sticky=E)
output = Label(width=15, bd=2, relief=SUNKEN)
output.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Row 2 controls
# Convert button
convert_button = Button(text="Convert", width=10, command=calculate)
convert_button.grid(row=2, column=0, padx=5, sticky=E)
tooltip.bind_widget(convert_button, msg="Click to convert the temperature")
# Clear button
clear_button = Button(text="Clear", width=10, command=clear)
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky=W)
tooltip.bind_widget(clear_button, msg="Click to clear all fields")
# Exit button
exit_button = Button(text="Exit", width=10, command=close_window)
exit_button.grid(row=2, column=2, padx=5, pady=5, sticky=W)
tooltip.bind_widget(exit_button, msg="Click to exit")

# Row 3 control
label_status = Label(window, width=90, borderwidth=1, relief=SOLID)
tooltip.bind_widget(label_status, msg="Displays status and error messages")
label_status.grid(row=4, columnspan=4, sticky=S)

# Hotkeys for the three main buttons.
window.bind("<Alt-c>", calculate)
window.bind("<Alt-l>", clear)
window.bind("<Alt-x>", close_window)

# Launch the window.
window.mainloop()
