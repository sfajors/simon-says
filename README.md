# simon-says
This is a simple implementation of the "Simon Says" game using the tkinter library for the graphical user interface. The game mechanics involve presenting the player with a sequence of colors which they then need to repeat back by clicking the corresponding color buttons. The sequence gets longer with each round.

# Here are some key components of this script
COLORS Dictionary: Defines a set of color codes paired with their respective color names.

GUI Components: Uses tkinter to create the main game window, color buttons, a message label, and a start button.

Game Logic:
add_to_sequence(): Adds a random color to the sequence.
highlight_button(): Highlights a button with a specific color for a given duration.
get_player_input(): Prepares the game to receive player input.
handle_button_click(): Handles the player's input when they click on a color.
start_new_round(): Starts a new round by clearing player input and preparing to display a new sequence.
display_sequence(): Shows the current sequence to the player.
start_game(): Initializes the game, clearing any existing sequences and starting a new round.

# How to launch the Game
Prerequisites:
- Ensure you have Python installed on your system. If not, download and install Python from the official website.
- Ensure you have the tkinter library available. Most standard Python installations come with tkinter included. However, if you find it's missing, you can install it using your package manager (e.g., apt-get on Debian-based systems, brew on macOS, etc.).

Download the Game:
- If you haven't already, download the simon-says.py script from the repository.

Run the Game:
- Navigate to the directory containing the simon-says.py script using your terminal or command prompt.
- Launch the game using the following command:
  ```bash
  python simon-says.py 

(Note: Depending on your system setup, you might need to use python3 instead of python.)

Play the Game:
- Once launched, you should see the game's user interface with various colored buttons.
- Click the "Start" button to begin playing. Follow the on-screen instructions and prompts.
