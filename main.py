def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    report(book_path, word_count, letter_count)

def sort_on(dict):
    return dict["num"]

def report(file_name, words, letters):
    print(f"-- Report for {file_name} --")
    print(f"There are {words} found in the file")
    list_of_letters =[]
    for letter in letters:
        list_of_letters.append({"name": letter, "num": letters[letter]})
    list_of_letters.sort(reverse=True, key=sort_on)
    for letters in list_of_letters:
        print(f"The '{letters["name"]}' character was used {letters["num"]} times")
    print("-- End of report --")
    
def count_letters(string):
    char_dict = {}
    for char in string:
        if char.isalpha():
            if char.lower() not in char_dict:
                char_dict[char.lower()] = 1
            else:
                char_dict[char.lower()] += 1
    return char_dict

def count_words(string):
    words = string.split()
    word_count = len(words)
    return word_count


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()