#!/usr/bin/env python
# encoding UTF-8

"""
Assignment 7 Task 1
Jon Nations 10 Feb 2016
"""


def palindrome():
    word = input("Enter a possible palindrome (no spaces): ")
    if word == word[::-1]:
        return True, print("This is a palindrome!")
    else:
        return False, print("This is not a palindrome")


def main():
    palindrome()


if __name__ == '__main__':
    main()
