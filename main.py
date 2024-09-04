import tkinter as tk
from tkinter import messagebox
from word_guess import WordGuess

class WordGuessGame:
    def __init__(self, root):
        self.root = root
        self.game_active = False  # Flag to prevent input when the game is resetting
        self.game = WordGuess(6, "myWords.txt")  # Initialize the game logic
        self.game.readFile()  # Load words from the file
        self.labels = []  # To store the label grid
        
        # Setup GUI elements
        self.setup_ui()
        self.reset_game()

    def setup_ui(self):
        """Sets up the GUI components."""
        self.root.title("Word Guess")
        self.root.config(bg="#dbdbdb")
        self.root.geometry("410x500")
        
        # Entry box for user input
        self.entry_box = tk.Entry(self.root, justify='center', bd=0, highlightthickness=0, relief='flat', font=("Arial", 18), width=10)
        self.entry_box.grid(row=99, column=0, columnspan=5, pady=(10, 5))
        
        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.get_word, highlightbackground="black", bd=1, highlightthickness=0, font=("Arial", 16, "bold"), relief='solid', height=2)
        self.guess_button.grid(row=100, column=0, columnspan=5, pady=5)
        
        # Create the grid for guesses
        for j in range(6):
            row = []
            for i in range(5):
                label = tk.Label(self.root, text=" ", font=("Arial", 24, "bold"), width=5, height=2, borderwidth=1, relief='solid', bd=0, bg="white")
                label.grid(row=j, column=i, padx=5, pady=5, sticky=tk.NSEW)
                row.append(label)
            self.labels.append(row)

    def reset_game(self):
        """Resets the game to its initial state."""
        self.game_active = False
        self.guess_button.config(state=tk.DISABLED)  # Disable interactions during reset

        # Clear the grid and reset the guess count
        for row in self.labels:
            for label in row:
                label.config(text=" ", bg="white")
        
        self.game.selectRandomWord()
        self.entry_box.delete(0, tk.END)  # Clear input box
        self.entry_box.focus()  # Focus on the input
        self.game.NUMBER_OF_USER_GUESSES = 1  # Reset the guess count
        self.game_active = True
        self.guess_button.config(state=tk.NORMAL)

    def game_over_popup(self, message):
        """Displays game over options."""
        self.game_active = False
        self.root.update()  # Force the GUI to update
        response = messagebox.askyesno("Game Over", message + "\nDo you want to play again?")
        if response:
            self.reset_game()
        else:
            self.root.quit()

    def get_word(self):
        """Handles the player's word input and checks against the solution."""
        if not self.game_active:
            return

        guessed_word = self.entry_box.get().strip()  # Strip whitespace
        self.entry_box.delete(0, tk.END)

        # Validate the guessed word (5 letters and present in the word list)
        if len(guessed_word) == 5 and guessed_word in self.game.eachWordAsElement:
            current_word_list = list(self.game.word.lower())
            guessed_word_list = list(guessed_word.lower())
            letter_count = {letter: current_word_list.count(letter) for letter in set(current_word_list)}

            matched_indices = []
            # First pass: Mark exact matches (green)
            for i in range(5):
                if guessed_word_list[i] == current_word_list[i]:
                    self.labels[self.game.NUMBER_OF_USER_GUESSES - 1][i].config(text=guessed_word[i].upper(), bg="#28a745")
                    matched_indices.append(i)
                    letter_count[guessed_word_list[i]] -= 1

            # Second pass: Mark partial matches (yellow)
            for i in range(5):
                if i not in matched_indices:
                    if guessed_word_list[i] in current_word_list and letter_count[guessed_word_list[i]] > 0:
                        self.labels[self.game.NUMBER_OF_USER_GUESSES - 1][i].config(text=guessed_word[i].upper(), bg="#ffeb3b")
                        letter_count[guessed_word_list[i]] -= 1
                    else:
                        self.labels[self.game.NUMBER_OF_USER_GUESSES - 1][i].config(text=guessed_word[i].upper())

            # Check if the player has won
            if guessed_word.lower() == self.game.word.lower():
                self.game_over_popup(f"Congrats! You guessed the word '{self.game.word}' in {self.game.NUMBER_OF_USER_GUESSES} tries.")
                return

            # Check if the player has used all guesses
            if self.game.NUMBER_OF_USER_GUESSES == self.game.guesses:
                self.game_over_popup(f"You were not able to guess the word '{self.game.word}' in {self.game.NUMBER_OF_USER_GUESSES} tries.")
                return

            self.game.NUMBER_OF_USER_GUESSES += 1
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid 5-letter lowercase word.")


# Tkinter setup
window = tk.Tk()
game = WordGuessGame(window)
window.mainloop()
