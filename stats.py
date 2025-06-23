import sys
def num_words(filepath):
    with open(sys.argv[1]) as b:
        book = b.read()
        words = book.split()
        word_count = len(words)
    return word_count

def get_book_text(filepath):
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

words = get_book_text(sys.argv[1])
word_count = num_words(sys.argv[1])



def num_characters():
    low_words = words.lower()
    character_count = {}

    for c in low_words:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1

def dict_sort():
    data = []
    characters = {}
    low_words = words.lower()

    for c in low_words:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    def sort(items):
        return items["num"]

    for key, value in characters.items():
        char_dict = {"char":key,"num":value}
        data.append(char_dict)

    data.sort(reverse=True, key=sort)
    return data
