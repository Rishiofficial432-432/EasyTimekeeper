import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')  # Format time as hours, minutes, seconds, and AM/PM
    label.config(text=string)          # Update label with current time
    label.after(1000, time)            # Call the time function every 1 second (1000 ms)

# Create and configure the label (clock display)
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

# Call the time function to initiate the clock update
time()

# Start the Tkinter event loop
root.mainloop()
