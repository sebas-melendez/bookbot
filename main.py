def get_book_text(pathsito):
    with open(pathsito) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words , char_stats, sort_chars
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
bookpath = "books/frankenstein.txt"
main()