from utils import *
from letter_frequency import frequency_df
import pandas as pd

# explore the words pool first by guessing several words with popular letters, then use this information to make meaningful guesses

def words_containing(letters, guesses):
    target = [g for g in guesses if all(l in g for l in letters)]
    return(target)

def guess_popular_letters(rank, guesses, frequency = frequency_df):
    first_letter = rank * 5
    last_letter = min(first_letter + 5, 26)
    word_contain = words_containing(list(frequency.iloc[range(first_letter, last_letter), 0]), guesses)
    if len(word_contain) == 0:
        return False
    else:
        current_guess = word_contain[0]
        return current_guess

def explore_first(word, guesses):
    guess_count = 0
    for i in range(6):
        guess_count += 1

        if i <= explore_turn and not guess_popular_letters(i, guesses, frequency_df) == False:
            current_guess = guess_popular_letters(i, guesses, frequency_df)
        else:
            current_guess = guesses[0]

        if current_guess == word:
            return guess_count
        
        guesses = filter_guesses(current_guess, word, guesses)

    return None

explore_turn = 2

run_and_save(explore_first, "explore_first_result.csv", answers, guesses)