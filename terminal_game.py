import random

def load_words(file_path):
    return open(file_path).read().split()

def valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses

def evaluate_guess(guess, word):
    str = ""
    for i in range(5):
        if guess[i] == word[i]:
            str += '\x1b[32m' + guess[i] + '\033[0m'

        elif guess[i] in word:
            str += '\x1b[33m' + guess[i] + '\033[0m'

        else:
            str += guess[i]

    return str

def wordle(answers, guesses):
    attempt = 1
    max_attempt = 6
    word = random.choice(answers)
    print('Wordle')
    print('Get 6 chances to guess a 5-letter word.')

    while attempt <= max_attempt:
        guess = input('Enter your ' + str(attempt) + '. guess: ')

        while not valid_guess(guess, guesses):
            print('Not in word list')
            guess = input('Enter your ' + str(attempt) + '. guess: ')

        print(evaluate_guess(guess, word))

        if guess == word:
            return print("Congratulations! Today's word is " + word + "!")

        attempt += 1
    
    print("Lost! Today's word is " + word + "!")

answers = load_words('answers.txt')
guesses = load_words('guesses.txt')

wordle(guesses, answers)