from tkinter import *
from tkinter.ttk import *
from time import strftime  # Importing necessary modules: Tkinter and time

# Create the user interface
root = Tk()
root.title("clock")  # Set the title of the window

# Define a function to update time on the UI
def time():
    string = strftime('%H:%M:%S %p')  # Get the current time in the desired format
    label.config(text=string)  # Set the text of the label to the current time
    label.after(1000, time)  # Schedule the time function to run again after 1 second (1000 milliseconds)

# Create a label widget to display the time
label = Label(root, font=("ds-digital", 80), background='black', foreground='cyan')
label.pack(anchor='center')  # Place the label in the center of the window

time()  # Call the time function to start displaying the time

mainloop()  # Start the Tkinter event loop to display the window
