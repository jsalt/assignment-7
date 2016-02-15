#!/usr/bin/env python
# utf-8

"""
Program to check whether given string is palindrome or not
Created by Pramod Pantha on 7 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
http://stackoverflow.com/questions/19368509/improving-python-palindrome-code
https://docs.python.org/3/howto/argparse.html
"""


import argparse


def palindrome(choice):
        choice_rev = choice[::-1]
        if choice == choice_rev:
            return True
        else:
            return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("palindrome_checker", help="string we want to check",
                        type=str)
    args = parser.parse_args()
    result = palindrome(args.palindrome_checker)

    print(result)

if __name__ == '__main__':
    main()
