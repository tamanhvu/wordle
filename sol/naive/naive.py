from utils import *
import pandas as pd

def naive_appoarch(word, guesses):
    guess_count = 0

    for i in range(6):
        current_guess = guesses[0]
        guess_count += 1
        if current_guess == word:
            return guess_count
        guesses = filter_guesses(current_guess, word, guesses)

    return None


answers = load_words('answers.txt')
guesses = load_words('guesses.txt')

run_and_save(naive_appoarch, "naive_result.csv", answers, guesses)