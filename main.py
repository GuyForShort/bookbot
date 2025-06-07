from stats import * 
from sys import * 
check=len(argv)
if check != 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)



def main():
    book=argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    word_count=get_num_words(book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count_dict={}
    letter_count_dict=count_letters(book)
    #print(letter_count_dict)
    unsorted_list=convert_to_list(letter_count_dict)
    #print(unsorted_list)
    sorted_list=list_sorter(unsorted_list)
    for a in sorted_list:
        print(f"{a["char"]}: {a["count"]}")

main()
