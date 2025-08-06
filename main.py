def get_book_text(pathsito):
    with open(pathsito) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(textazo):
    splitlist = str.split(textazo)
    return len(splitlist)


def main():
    textito = get_book_text("books/frankenstein.txt")
    print(f" {get_num_words(textito)} words found in the document")
    return
main()