import sys
from stats import get_num_words , char_stats, sort_chars
def get_book_text(pathsito):
    with open(pathsito) as f:
        file_contents = f.read()
        return file_contents

def main():
    textito = get_book_text(bookpath)
    print("======BOOKBOT======")
    print(f"Analyzing book found at {bookpath} ...")
    print("------- Word Count -------")
    print(f" Found {get_num_words(textito)} total words")
    print("------- Character Count -------")
    surtidito=(sort_chars(char_stats(textito)))
    for items in surtidito:
        print(f"{items["char"]}: {items["num"]}")
    return

if len(sys.argv) == 2:
    bookpath = sys.argv[1]
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#books/frankenstein.txt
