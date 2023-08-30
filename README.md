# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
## Classes:
### Hangman

## Hangman Methods:
        __init__: 
            Initialises the class and passes word_list and num_lives(default = 5) as arguments. Following attriubutes are initialised:
                -word: The word to be guessed, picked randomly from the word_list.
                -word_guessed: A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
                -num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
                -num_lives: int - The number of lives the player has at the start of the game.
                -word_list: list - A list of words
                -list_of_guesses: list - A list of the guesses that have already been tried.

        check_guess:
            Checks the character is in 'word'. If it is, the letter replaces the corresponding '_' in 'word_guessed', and 'num_letters' drops by 1. Else, it rerequests and input and reduces 'num_lives' by 1.
        
        ask_for_input:
            Checks the character that is entered is alphabetical, is a single character. If it, it runs 'check_guess'. If the character has previously been guessed or is invalid, input is rerequested.


## Functions:
    play_game:
        Sets the number of lives and initialises an instance of the Hangman class. Runs the game until the player exhausts their lives or they successfully guess the word