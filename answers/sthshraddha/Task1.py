#!/usr/bin/env python

"""
"able was i ere i saw elba" is a well_known palindrome. Write a generalized
program that proves this phrase is a palindrome. Because the program is
generalized, it should also prove that any other palindromes are actually
palindromes and it should prove when phrases or words are not palindromes.
Be sure to write your program such that this is the case. And, be sure that
your argument takes any palindrome on the command line as input (i.e., use the
argparse module). Write the program to include a main() function and the ifmain
statement. The main() function should call the function or functions that you
create to test for "palindrome_ness".

Credit url: http://pymbook.readthedocs.org/en/latest/strings.html
Date accessed: February 9th, 2016.

Created by Shraddha Shrestha on February 10, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

import argparse


def parser():
    parser= argparse.ArgumentParser()
    parser.add_argument("phrase", type=str, help="check for palindrome")
    args = parser.parse_args()
    return args.phrase


def palindrome():
    forward = parser()
    reverse = str(forward)[::-1]
    if forward == reverse:
        print("YES, string is a palindrome!")
    else:
        print("NOT a palindrome!")


def main():
    parser()
    palindrome()


if __name__ == '__main__':
    main()
