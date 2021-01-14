from random import random
from math import floor

secret_word = ""
letters_left = 0
hangman_guesses_left = 6
letters_guessed = []
errors = 0
underscored_secret_word = ""
secret_words = ["development", "random", "postman", "mountain", "python", "wrong", "javascript", "software", "engineer"]

hangman1 = '''
______
|    |
|    O
|
|
|__________
'''
hangman2 = '''
______
|    |
|    O
|    |
|
|__________
'''
hangman3 = '''
______
|    |
|    O
|   /|
|
|__________
'''
hangman4 = '''
______
|    |
|    O
|   /|\\
|
|__________
'''
hangman5 = '''
______
|    |
|    O
|   /|\\
|   /
|__________
'''
hangman6 = '''
______
|    |
|    O
|   /|\\
|   / \\
|__________
'''
hangman_table = [
  f'\n{hangman6}\n',
  f'\n{hangman5}\n',
  f'\n{hangman4}\n',
  f'\n{hangman3}\n',
  f'\n{hangman2}\n',
  f'\n{hangman1}\n'
]

def game_init():
    global secret_word
    global letters_left
    global hangman_guesses_left
    global letters_guessed
    global errors
    global underscored_secret_word

    random_index = floor(random() * 6)
    secret_word - secret_words[random_index]
    letters_left = len(secret_word)
    hangman_guesses_left = 6 
    letters_guessed = []

    i = 0 
    while i < len(secret_word):
        underscored_secret_word = underscored_secret_word + "_ "
        i += 1

def win():
    print('You won!')
    print(f'The word was [{secret_word}')

def lose():
    print('HMAN: :(')
    print('The secret word was {secret_word}')

def add_to_guesses(guess):
    letters_guessed.append(guess)

def success(guess):
    global underscored_secret_word
    global win
    print('Correct')
    add_to_guesses(guess)
    index = 0
    for letter in secret_word:
        if letter == guess:
            if index == 0
            underscored_secret_word = guess + underscored_secret_word[1:]
            elif index < (len(secret_word) - 1)
            underscored_secret_word = underscored_secret_word[0: (index * 2)] + guess + " " + underscored_secret_word[(index * 2 + 2)]
            else:
                underscored_secret_word = underscored_secret_word[:-2] + guess
            index += 1

            for letter in underscored_secret_word:
                if letter == '_':
                    continue_game()
                    return 
            win()                      

 def print_hangman(incorrect_guesses_left):
     print(hangman_table[incorrect_guesses_left]) 

def failure(guess):
    global hangman_guesses_left
    add_to_guesses(guess)
    hangman_guesses_left -= 1
    print_hangman(hangman_guesses_left)
    continue_game()

def already_guessed():
    print('You already guessed that')
    continue_game()
    
def continue_game():
    global errors
    print(f'You have {hangman_guesses_left} guesses left.')
    print(f"You have guessed {letters_guessed}")
    print(f"The word you need: {underscored_secret_word}")

    if hangman_guesses_left > 0:
        guess = input('Guess a letter:\n').lower()
        if guess == secret_word:
            win()
            return
        if len(guess) > 1 and errors < 1:
            print('It looks like you accidentally entered more than one character or you guessed the wrong word')
            errors += 1
            continue_game()
            return
        try: 
            int(guess)
            print('It looks like you accidentally entered a number.')
            errors += 1
            continue_game()
            return
        except ValueError:
            pass
        if guess in letters_guessed:
            already_guessed()
            return
        for letter in secret_word:
            if letter == guess:
                success(guess)
                return
            failure(guess)
            return         
        else:
            lose()

looping = True
game_init()
continue_game()

while looping:
    should_continue = input('Would you like to play again? yes or no\n').lower()
    if should_continue == 'yes' or should_continue == 'y':
        game_init()
        continue_game()
    elif should_continue == 'no' or should_continue == 'n':
        print('Thaks for playing!')
        looping = False
    else:
        print("I'm not sure whether you mean yes or no.\n")       


