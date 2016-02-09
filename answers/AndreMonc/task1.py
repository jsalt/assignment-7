# !/usr/bin/env python
# encoding: utf-8


"""
My palindrome-checking program
Created by Andre Moncrieff on 9 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.

This program verifies that a word or phrase is a palindrome. If input contains 
spaces than quotes must be used on either side of input to indicate that it is
one argument. Works on words or numbers. Punctuation must also be palindromic.
"""


import argparse


def format_string(raw):
    formatted = str(raw.replace(" ", "").lower())
    return formatted


def reverse_string(raw):
    fixed = format_string(raw)
    reverse = fixed[::-1]
    return reverse


def parser():   
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", help="Add a potential palindrome in order" 
                       + " to verify it as such. Punctuation must also be" +
                       " palindromic.", type=str)
    args = parser.parse_args()
    return args.candidate


def palindrome_checker(candidate = parser()):   
    if reverse_string(candidate) == format_string(candidate):
        return "Yay! Your input is a palindrome"
    else:
        return "Your input is NOT a palindrome"


def main():
    output = palindrome_checker()
    print(output)       
   
   
if __name__ ==  '__main__':
    main()
    






    
    



    

