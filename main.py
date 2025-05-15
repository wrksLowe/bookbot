from stats import get_book_text
from stats import count_words
from stats import character_count
from stats import sort_characters
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
path = sys.argv[1]
def main():
    book_path = path
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    chars = character_count(book_text)
    sorted_chars = sort_characters(chars)
    
    # Print the report according to the required format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")
    print(sys.argv)



main()


