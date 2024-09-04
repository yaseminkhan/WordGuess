import random

class WordGuess:
    def __init__(self, guesses, file):
        self.guesses = guesses  # Maximum number of guesses
        self.file = file  # Path to the file
        self.eachWordAsElement = []  # List to store the words
        self.currentWord = ""  # The current word selected
        self.NUMBER_OF_USER_GUESSES = 1  # Track the number of guesses used

    def readFile(self):
        """Reads the file and stores each word as an element in a list."""
        try:
            with open(self.file, "r") as fileHandler:
                self.eachWordAsElement = [word.strip() for word in fileHandler.readlines() if word.strip()]
            if not self.eachWordAsElement:
                raise ValueError("The word list is empty.")
        except (FileNotFoundError, ValueError) as e:
            print(f"Error reading file: {e}")

    def selectRandomWord(self):
        """Selects a random word from the list."""
        if self.eachWordAsElement:
            self.currentWord = random.choice(self.eachWordAsElement)
        else:
            print("No words available to select.")

    @property
    def word(self):
        """Returns the current word."""
        return self.currentWord
