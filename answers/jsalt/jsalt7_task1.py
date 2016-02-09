#!/usr/bin/env python
# utf-8

"""
Assignment 7
Task 1 Program: Palindrome Checker
Jessie Salter
9 February 2016
"""

import argparse

import re


def prompt():
    '''This function takes user input'''
    parser = argparse.ArgumentParser()
    parser.add_argument("palindrome", help="A phrase you wish to evaluate for \
    palindrome status; must be in quotes", type=str)
    args = parser.parse_args()
    return args.palindrome


def rem_space():
    '''This function removes spaces from the input phrase'''
    starter = prompt()
    phrase = re.sub(r'\s+', '', starter)
    return phrase


def palidrome_check():
    '''This function evaluates whether a phrase is a palindrome'''
    phrase = rem_space()
    if str(phrase) == (str(phrase)[::-1]):
        print("This phrase is a palindrome")
    else:
        print("This phrase is not a palindrome")


def main():
    prompt()
    rem_space()
    palidrome_check()


if __name__ == '__main__':
    main()
