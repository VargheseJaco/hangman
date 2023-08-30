#%%
import random

word_list = ['lychee', 'mango', 'raspberry', 'strawberry', 'orange','mango']

class Hangman:

    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(list(set(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            index = 0
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[index] = guess
                    print(f'Letters guessed: {self.word_guessed}')
                index += 1
            self.num_letters -= 1
            print(f'Number of letters left to guess: {self.num_letters}')
                
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        # while True:
        guess = input('Enter a single letter:')
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:   
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            # break
            

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives > 0 and game.num_letters == 0:
            print('You won!')
            break
        elif game.num_lives == 0:
            print('Sorry! You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            
play_game(word_list)
       
# %%
