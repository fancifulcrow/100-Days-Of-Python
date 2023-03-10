import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict =  {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name:").upper()
alphabet_list = [nato_alphabet_dict[letter] for letter in name]
print(alphabet_list)

