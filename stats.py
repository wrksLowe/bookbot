
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

def character_count(book_text):
    char_dict={}
    lower_chars=[]
    letters=[] #list of letters (lowercase)
    #convert text into list of letters
    lower_chars = list(book_text.lower())
    for char in lower_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_characters(unsorted_dict):
    dict_to_list = []
    for char, count in unsorted_dict.items():
        # Only include alphabetical characters
        if char.isalpha():  # This checks if char is a letter (a-z, A-Z)
            dict_to_list.append({"char": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    dict_to_list.sort(reverse=True, key=sort_on)
    return dict_to_list

    

        