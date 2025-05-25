from string import *

def get_num_words(bookpath):
    with open(bookpath) as file:
        book = file.read()
        words = book.split()
        word_count = 0
        for word in words:
            word_count += 1

        print(f"{word_count} words found in the document")
    return

def characters():
    output =list(printable)
    return output

def count_letters(bookpath):
    char_list=characters()
    counted_letters={}
    letter_count = 0
    with open(bookpath) as file:
        book = file.read()
        lcase_book = book.lower()
        booklist = list(lcase_book)
        for char in char_list:
            #print(char)
            for letter in booklist:
                if char == letter:
                    letter_count += 1
            #print(letter_count)        
            counted_letters[char]=letter_count
            #print(counted_letters)
            letter_count = 0
    return counted_letters