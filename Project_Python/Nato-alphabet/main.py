import pandas
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (key, row) in df.iterrows()}
print(phonetic_dict)

# version 1
# correct_word = True
# while correct_word:
#     word = input("Enter a word: ").upper()
#     try:
#         output = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         correct_word = False
#         print(output)

# version 2
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        correct_word = False
        print(output)

generate_phonetic()