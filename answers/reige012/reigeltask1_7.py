#!/usr/bin/env python
# #encoding: utf-8

"""
This program takes a sentence or phrase as input from the user and then determines
if it is a palindrome (words that read as the same phrase backwards and forwards).
The program then lets the user know if it is or isn't a palindrome.

***User input must have quotations around it for the program to recognize it as
a phrase to be checked***

Created by Alicia Reigel. 5 February 2016
Copyright Alicia Reigel. Louisiana State University. 5 February 2016. All rights
reserved.

 """

import argparse
import string

def palindrome_input():
    """this function takes input from the user"""
    parser = argparse.ArgumentParser(
            description="""Determine if a phrase is a palindrome"""
        )
    parser.add_argument(
            'palindrome_phrase',
            type=str,
            help='Enter the phrase you want to check with quotes around it.'
        )
    args = parser.parse_args()
    return args.palindrome_phrase
        #above statement takes the user input and returns it to the main loop.

def is_it_a_palindrome(x):
    """this function tests if the input is a palindrome or not"""
    x=str(x)
    lower_case_phrase=str.lower(x)
        #makes the string lower case
    reverse_string=(lower_case_phrase[::-1])
        #reverses the order of the string
    if list(lower_case_phrase) == list(reverse_string):
            #changes the phrases to lists for comparison and prints an answer
        print("Yay! Your phrase is so cool! It's a palindrome!")
    else:
        print("Sorry, this phrase is not a palindrome. ")

def main():
    user_palindrome=palindrome_input()
    new_x=user_palindrome.replace(" ", "")
        #this removes spaces from the user input.
    for c in string.punctuation:
        new_x= new_x.replace(c,"")
            #this removes any punctuation that would interfer with palindrome recognition
    is_it_a_palindrome(new_x)

if __name__ == '__main__':
    main()
