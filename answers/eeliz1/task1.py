#!/usr/bin/env python
# encoding: utf-8

"""
Assignment 7, Task 1

Elisa Elizondo
11 Feb. 2016

This program evaluates whether arguments entered by the user are palindromes or not.
"""

import argparse

##palindrome_or_no evaluates whether the argument, s, is a palindrome or not.
##If it is, it returns the answer "True", if not, it returns "False".
##source for function code:
##http://stackoverflow.com/questions/11496637/python-recursive-check-to-determine-whether-string-is-a-palindrome##
def palindrome_or_no(s):
    if s == '':
        return True
    else:
        if (ord(s[0]) - ord(s[len(s)-1])) == 0:
            return palindrome_or_no(s[1:len(s)-1])
        else:
            return False

##Defines position argument "string" and option "help" with argparse
##source: https://www.youtube.com/watch?v=rnatu3xxVQE
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help = "Evaluates if argument is a palindrome. If multiple words, use double quotation marks around phrase.",
                        type = str)
    args = parser.parse_args()

    result = print(palindrome_or_no(args.string))


if __name__ == '__main__':
    main()
