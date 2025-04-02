import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

word_input = input("Enter a word: ").upper()
# print(word_input)

nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

word_coded = [nato_dict[letter] for letter in word_input]
print(word_coded)
