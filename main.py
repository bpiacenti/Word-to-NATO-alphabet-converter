import pandas

nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')

def nato_conversion():
    word_input = input("Enter a word: ").upper()
    # print(word_input)
    try:
        nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
        # print(nato_dict)
        word_coded = [nato_dict[letter] for letter in word_input]
    except KeyError:
        print("Please use only letters in the alphabet.")
        nato_conversion()
    else:
        print(word_coded)

nato_conversion()