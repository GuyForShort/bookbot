def get_num_words(bookpath):
    with open(bookpath) as file:
        book = file.read()
        words = book.split()
        word_count = 0
        for word in words:
            word_count += 1

        print(f"{word_count} words found in the document")
    return
