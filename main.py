from stats import number
from stats import character
from stats import get_alpha_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    counted = number(text)
    #print(f"{counted} words found in the document")
    char_count = character(text)
    #print(char_count)
    alpha_list = get_alpha_list(char_count)
    alpha_list.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {counted} total words")
    print("--------- Character Count -------")
    index = 0 
    for item in alpha_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def sort_on(items):
    return int(items["num"])

  
main()