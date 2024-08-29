import sys
import termcolor
import random

class WordGuess:
    CURRENT_WORD = ""
    NUMBER_OF_USER_GUESSES = 1

    # This function creates two instance variables that are used to keep track of the maximum number of guesses allowed and to access the txt file.
    def __init__(self, guesses, file):
        self.guesses = guesses
        self.file = file

    # This function opens the file and creates a list of words from the txt file where every word is an element in the list.
    def readFile(self):
        fileHandler = open(self.file,"r")
        self.eachWordAsElement = fileHandler.readlines()
        fileHandler.close()

    # This function randomly selects a word from the txt file.
    def selectRandomWord(self):
        self.CURRENT_WORD = random.choice(self.eachWordAsElement)

    # This function chosses a word from the txt file and prints the word as well as the length of the word.
    def removeNewLineFromWord(self):
        self.currentWord = self.CURRENT_WORD.rstrip()
        print(self.currentWord)
        print(len(self.currentWord))


    # This function contains a loop that gets continuous user input (guesses) and sorts them into if/elif/else statements that determine whether each letter is correct or not.
    def playWordGuess(self):
        while (self.NUMBER_OF_USER_GUESSES <= self.guesses):
            userInput = input("\n Guess Number {}:".format(self.NUMBER_OF_USER_GUESSES))
            # Takes input/guesses from the user.
            for i in range(len(self.currentWord)):
                if (self.currentWord[i]==userInput[i]):
                    print(termcolor.colored(userInput[i], 'green'), end="")
                    # If the correct letter is guessed and is in the correct spot for the word then the letter turns green.
                elif (userInput[i] in self.currentWord):
                    print(termcolor.colored(userInput[i], 'yellow'), end="")
                    # If the correct letter is guessed but not in the correct spot then the letter turns yellow.
                else:
                    print(userInput[i], end="")
                    # If the letter is not in the word than it is printed in no specific colour.
            if (self.currentWord==userInput):
                print("\n Congrats on getting the word which was {}! You got it in {} tries.".format(self.currentWord,self.NUMBER_OF_USER_GUESSES))
                sys.exit()
                #If the correct word is guessed then the above statement is printed and the program is safely exited
            elif (self.NUMBER_OF_USER_GUESSES==self.guesses and not self.currentWord==userInput):
                print("\n You were not able to guess {} in {} tries. Try again!".format(self.currentWord, self.NUMBER_OF_USER_GUESSES))
                sys.exit()
                #If the correct word is not found in 6 tries, then the above statement is printed and the program is safely exited.
            self.NUMBER_OF_USER_GUESSES+=1


# Code that instantiates your WordGuess class and runs it
game = WordGuess(6, "myWords.txt")
game.readFile()
game.selectRandomWord()
game.removeNewLineFromWord()
game.playWordGuess()
