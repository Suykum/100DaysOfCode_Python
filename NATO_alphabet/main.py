import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for(index, row) in data.iterrows()}

is_continue = True
while is_continue:
    user_input = input("Enter a word: ").upper()
    if user_input == "Q":
        is_continue = False
    else:
        words = [data_dict[letter] for letter in user_input]
        print(words)

