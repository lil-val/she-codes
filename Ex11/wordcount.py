#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Wordcount exercise
Google's Python class
----------------------
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. Implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. Implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

----------------------
Remarks:
1. Use str.split() (no arguments) to split on all whitespace.
2. Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
3. Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def words_counter(filename):
    # builds dictionary of word1: count_word1, word2: count_word2, etc
    counter = {}
    my_file = open(filename, 'r')
    for line in my_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
    my_file.close()
    return counter


def print_words(filename):
    # prints in different lines word1: count1 sorted alphabetically
    counter = words_counter(filename)
    words_list = sorted(counter.keys())
    for word in words_list:
        print(word, counter[word])


def print_top(filename):
    # sort dictionary per values in descending order and return first 20
    counter = words_counter(filename)
    words_list_by_value = [(v, k) for k, v in counter.items()]
    sorted_words_list_by_value = sorted(words_list_by_value, reverse=True)
    print(sorted_words_list_by_value[:20])


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    choice = 0
    first = True
    while not (choice == 1 or choice == 2):
        if not first:
            print("Invalid Choice: " + choice + "\n")
        first = False
        choice = int(input("What whould you like to do?\n1 count\n2 topcount\nEnter your chioce:\n"))
        filename = input("Please insert the file path:\n")
    do_choice(choice, filename)


def do_choice(choice, filename):
    option = choice
    if option == 1:
        print_words(filename)
    elif option == 2:
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
