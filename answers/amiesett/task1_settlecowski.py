#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 7 Task 1

Amie Settlecowski
11 Feb. 2016

This program tests whether phrases/wordds entered by the user are/are not
palindromes.

**TO USE**
python ~/task1_settlecowski.py --phrase "WORD/PHRASE"
"""


import argparse


def input_phrase():
    # parses user input and returns phrase to main
    # source: https://youtu.be/rnatu3xxVQE
    parser = argparse.ArgumentParser()
    parser.add_argument("--phrase",
        required=True,
        help="Phrase tested for palindrome-ness",
        type=str)
    args = parser.parse_args()
    return args.phrase


def palindrome_ness(phrase):
    # returns true if phrase is palindrome or false if not
    # convert phrase to all lowercase
    phrase = phrase.lower()
    # reverse input phrase, source:
    # (http://stackoverflow.com/questions/931092/reverse-a-string-in-python,
    # accessed 9 Feb. 2016)
    test = phrase[::-1]
    # test whether input phrase and the reverse are identical
    if phrase == test:
        return True
    else:
        return False


def main():
    # read in phrase from user
    phrase = input_phrase()
    # phrase = "Sore was I ere I saw Eros"
    # test input phrase for pallindrome-ness
    if palindrome_ness(phrase):
        print("Cool palindrome!")
    else:
        print("Sorry, not a palindrome :(")

if __name__ == '__main__':
    main()
