def get_book_text(filepath):
    file_contents= ""
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents


def count_words(text):
    length=0
    split_text=[]
    split_text=text.split()
    length=len(split_text)
    return length   



def main():
    book_text=""
    count=0
    book_text=get_book_text("books/frankenstein.txt")
    count=count_words(book_text) 
    return print(f"{count} words found in the document")

    


main()


