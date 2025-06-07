from stats import * #get_num_words



def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    word_count=get_num_words("./books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count_dict={}
    letter_count_dict=count_letters("./books/frankenstein.txt")
    #print(letter_count_dict)
    unsorted_list=convert_to_list(letter_count_dict)
    #print(unsorted_list)
    sorted_list=list_sorter(unsorted_list)
    for a in sorted_list:
        print(f"{a["char"]}: {a["count"]}")

main()
