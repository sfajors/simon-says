import tkinter as tk
from tkinter import messagebox
import random

# Colors
COLORS = {
    'R': 'red',
    'G': 'green',
    'Y': 'yellow',
    'B': 'blue',
    'P': 'purple',
    'O': 'orange',
    'C': 'cyan',
    'M': 'magenta'
}

# Create the main game window
root = tk.Tk()
root.title("Simon Says")

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create a label to display messages to the player
message_label = tk.Label(root, text="Click 'Start' to begin!", font=("Helvetica", 16))
message_label.pack(pady=20)

# Create Canvases and Rectangles for each color
color_buttons = {}
rect_buttons = {}
for color_code, color_name in COLORS.items():
    canvas = tk.Canvas(button_frame, width=80, height=40, bg="white", highlightthickness=0)
    rectangle = canvas.create_rectangle(5, 5, 75, 35, fill="white")
    canvas.grid(row=0, column=list(COLORS.keys()).index(color_code), padx=5, pady=5)
    color_buttons[color_code] = canvas
    rect_buttons[color_code] = rectangle

# Create a "Start" button
start_button = tk.Button(root, text="Start", font=("Arial", 16))
start_button.pack(pady=20)

# Initialize game variables
sequence = []
player_input = []
game_in_progress = False

# Function to add a random color to the sequence
def add_to_sequence():
    color = random.choice(list(COLORS.keys()))
    sequence.append(color)
    get_player_input()

# Function to highlight a button
def highlight_button(color, duration=2):
    canvas = color_buttons[color]
    rectangle = rect_buttons[color]
    original_color = COLORS[color]
    canvas.itemconfig(rectangle, fill=original_color)
    root.update()
    root.after(duration * 1000, lambda: canvas.itemconfig(rectangle, fill="white"))

# Function to get player input after displaying the sequence
def get_player_input():
    global game_in_progress
    game_in_progress = True

# Function to handle player's input
def handle_button_click(color):
    global player_input
    highlight_button(color)  # Show the color the user has clicked
    if game_in_progress:
        player_input.append(color)
        if player_input[-1] != sequence[len(player_input) - 1]:
            end_game()
        elif len(player_input) == len(sequence):
            start_new_round()

# Function to start a new round
def start_new_round():
    global player_input
    player_input = []
    message_label.config(text="Starting new round...")
    root.after(1500, begin_new_round)  # 2-second pause before starting a new round

def begin_new_round():
    add_to_sequence()
    message_label.config(text=f"Sequence length: {len(sequence)}")
    display_sequence()

def reset_all_buttons_to_white():
    for color in COLORS.keys():
        canvas = color_buttons[color]
        rectangle = rect_buttons[color]
        canvas.itemconfig(rectangle, fill="white")

# Function to end the game
def end_game():
    global game_in_progress
    game_in_progress = False
    messagebox.showinfo("Simon Says", "Game Over!")
    message_label.config(text="Click 'Start' to begin!")
    start_button.config(state=tk.NORMAL)

# Function to display the current sequence
current_index = 0
def display_next_color():
    global current_index
    if current_index < len(sequence):
        color = sequence[current_index]
        highlight_button(color)
        current_index += 1
        root.after(2500, display_next_color)
    else:
        current_index = 0
        reset_all_buttons_to_white()

def display_sequence():
    global current_index
    current_index = 0
    display_next_color()

# Function to start the game
def start_game():
    global game_in_progress
    game_in_progress = True
    sequence.clear()
    start_new_round()
    start_button.config(state=tk.DISABLED)

# Bind the Canvases to the handle_button_click function
for color_code in COLORS.keys():
    color_buttons[color_code].bind("<Button-1>", lambda event, color=color_code: handle_button_click(color))

# Bind the start button to the start_game function
start_button.config(command=start_game)

root.geometry("850x350")
root.mainloop()
