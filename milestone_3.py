#%%
import random

word_list = ['lychee', 'mango', 'raspberry', 'strawberry', 'orange','mango']
word = random.choice(word_list)
# print(word_list.count('lychee'))

def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input('Enter a single letter:')
        if len(guess) == 1 and guess.isalpha():
            break
        else:   
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

# ask_for_input()


# %%
