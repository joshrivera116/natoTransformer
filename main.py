import pandas

nato = pandas.read_csv('nato_phonetic_alphabet.csv')
new_words = {row.letter: row.code for (index, row) in nato.iterrows()}


def generate():
    in_word = input('Word: ').upper()
    try:
        new_word = [new_words[lett] for lett in in_word]
    except KeyError:
        print('Invalid entry, please input a word or name')
        generate()
    else:
        print(new_word)

generate()