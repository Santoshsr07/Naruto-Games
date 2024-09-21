import subprocess
import os
import tkinter as tk
from PIL import Image, ImageTk
def select_option(option):
    global selected_option
    selected_option = option
    option_label.config(text=f"Selected option: {selected_option}")
    
    # Paths for the selected options
    if option == "Naruto vs Sasuke":
        script_path = r"naruto/Basic Movements/NVS.py"
        subprocess.run(["python", script_path])
    elif option == "Naruto Runner":
        script_path = r"NarutoRunnerPygame-main/main.py"
        subprocess.run(["python", script_path])
    else:
        pass  # No action for other options

# Create the main window
root = tk.Tk()
root.title("Select Options")

# Set window size
root.geometry("700x500")

# Load and set the background image
bg_image = Image.open("bg1.png").resize((700, 500))  # Resize to fit window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget for the background image
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)  # Cover the whole window

# Define a variable to store the selected option
selected_option = None

# Button size settings
button_width = 20
button_height = 2

# Create a frame to center-align buttons
button_frame = tk.Frame(root, bg=root.cget('bg'))  # Use the same color as the main window
button_frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window

# Create and pack option buttons with no background color in the frame
button1 = tk.Button(button_frame, text="Naruto vs Sasuke", width=button_width, height=button_height, command=lambda: select_option("Naruto vs Sasuke"), bg=root.cget('bg'))
button1.pack(pady=10, padx=10)

button2 = tk.Button(button_frame, text="Naruto Runner", width=button_width, height=button_height, command=lambda: select_option("Naruto Runner"), bg=root.cget('bg'))
button2.pack(pady=10, padx=10)

# Label to display the selected option
option_label = tk.Label(root, text="Selected option: None", bg="white")
option_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
