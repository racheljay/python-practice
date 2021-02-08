import random
from words import words
import string  # library that lets us import common string characters as a unit

# first we need to get rid of any words that wont work for hangman
# get rid of anything with non viable characters


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# sets are used to store multiple items in a single variable
# they are unordered and un-indexed
# so... an object basically?

def hangman():
    word = get_valid_word(words)
    # letters in the word to keep track of what's been guessed
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # starts empty to store what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word guess is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away a life if wrong guess
                print('Letter is not in this word')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again')

        else:
            print('This is not a valid character.')
    # gets here when let(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You have died, sorry. The word was', word)
    else:
        print('You have guess the word', word, '!!')

hangman()

# user_input = input('Type something:')
# print(user_input)
