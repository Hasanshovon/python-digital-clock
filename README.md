# Digital Clock using Tkinter

This Python script creates a simple digital clock using the Tkinter library. It displays the current time in hours, minutes, seconds, and AM/PM format.
![clock-output](https://github.com/Hasanshovon/python-digital-clock/assets/26182608/ebe079a3-a635-4268-bf25-d9df5e4e37a7)


## Requirements

- Python 3.x
- Tkinter (usually included in Python's standard library)

## Usage

1. Ensure you have Python installed.
2. Run the script `main.py`.
3. A window will appear showing the digital clock.

## Code Explanation

- `from tkinter import *`: Imports the Tkinter library for creating the GUI.
- `from tkinter.ttk import *`: Imports additional Tkinter widgets.
- `from time import strftime`: Imports the `strftime` function to retrieve system time.

- `root = Tk()`: Creates the main window for the clock.
- `root.title("clock")`: Sets the title of the window to "clock".

- `def time()`: Function to update the time on the UI every second.
- `string = strftime('%H:%M:%S %p')`: Retrieves the current time in the specified format.
- `label.config(text=string)`: Updates the label text with the current time.
- `label.after(1000, time)`: Schedules the `time()` function to run again after 1 second.

- `label = Label(root, font=("ds-digital", 80), background='black', foreground='cyan')`: Creates a label widget to display the time.
- `label.pack(anchor='center')`: Places the label in the center of the window.

- `time()`: Starts displaying the time.
- `mainloop()`: Initiates the Tkinter event loop to display the window.

## Note

- Make sure the font 'ds-digital' is available on your system or change it to a different available font if required.

Feel free to modify the script or customize the UI according to your preferences!

For any issues or improvements, please feel free to raise an issue or submit a pull request.
"# python-digital-clock" 
