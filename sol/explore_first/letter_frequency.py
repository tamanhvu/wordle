from enviroment import *

# frequency of each letter in words
letters_list = list(map(chr, range(97, 123)))
letter_count = list()

for l in range(len(letters_list)):
    count = list()
    for g in range(len(guesses)):
        count_in_word = guesses[g].count(letters_list[l])
        count.append(count_in_word)
    letter_count.append(sum(count))

frequency = {
    'letter': letters_list,
    'count': letter_count
}
frequency_df = pd.DataFrame(frequency)
frequency_df = frequency_df.sort_values(by='count', ascending=False)
