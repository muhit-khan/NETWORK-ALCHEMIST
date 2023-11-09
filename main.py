import tkinter as tk
from tkinter import ttk
from subprocess import Popen, PIPE
from tkinter import simpledialog

# Define the commands
commands = ["ipconfig /all", "ping", "tracert", "nslookup", "ipconfig /flushdns", "ipconfig /release", "netsh int ip reset", "netsh winsock reset"]

def run_command():
    command = selected_command.get()
    if command in ["ping", "tracert", "nslookup"]:
        address = simpledialog.askstring("Input", "Enter Address:", parent=root)
        if address is not None:
            command = command + " " + address
    process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    output, error = process.communicate()
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, output)

# Create the main window
root = tk.Tk()
root.title("Network Alchemist")  # Set the window title

# Create a dropdown menu
selected_command = tk.StringVar()
command_menu = ttk.Combobox(root, textvariable=selected_command)
command_menu['values'] = commands
command_menu.current(0)
command_menu.pack()

# Create a button to run the command
run_button = tk.Button(root, text="Run Command", command=run_command)
run_button.pack()

# Create a text box for the output
output_text = tk.Text(root)
output_text.pack()

# Start the main loop
root.mainloop()