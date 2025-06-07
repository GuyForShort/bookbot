from string import *

def get_num_words(bookpath):
    with open(bookpath) as file:
        book = file.read()
        words = book.split()
        word_count = len(words)
    return word_count

def count_letters(bookpath):

    char_list={}
    letter_count = 0
    with open(bookpath) as file:
        book = file.read()
        lcase_book = book.lower()
        booklist = list(lcase_book)

        for letter in booklist:
            if letter.isalpha():
                if letter in char_list:
                    char_list[letter] += 1 
                else:
                    char_list[letter] = 1


    return char_list

def convert_to_list(dict_in):
    listdict=[]
    for letter in dict_in:
        count=dict_in[letter]
        listdict.append({"char": letter, "count": count})
    return listdict

def sort_on(dict):
    return dict["count"]


def list_sorter(unsorted_list):
    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list
