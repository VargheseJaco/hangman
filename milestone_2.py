#%%
import random

word_list = ['lychee', 'mango', 'raspberry', 'strawberry', 'orange']
word = random.choice(word_list)
guess = input('Enter a single letter:')


if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print("Oops! That is not a valid input.")

print(word)
print(word_list)
# %%
