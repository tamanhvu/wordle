import pandas as pd

def load_words(file_path):
    return open(file_path).read().split()

answers = load_words('../data/answers.txt')
guesses = load_words('../data/guesses.txt')

def valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses

def filter_guesses(guess, word, guesses):
    for i in range(5):
        if guess[i] == word[i]:
            guesses = [w for w in guesses if w[i] == guess[i]]

        elif guess[i] in word:
            guesses = [w for w in guesses if guess[i] in w and w[i] != guess[i]]

        else:
            guesses = [w for w in guesses if guess[i] not in w]

    return guesses

def run_and_save(strategy, filename, answers, guesses):
    results = [strategy(a, guesses) for a in answers]

    df = pd.DataFrame({
        "word": answers,
        "guess_count": pd.array(results, dtype="Int64"),
    })
    df.to_csv(filename, index=False)
    return df