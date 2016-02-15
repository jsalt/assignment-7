#!/usr/bin/env python
# encoding: utf-8

"""
My 1st program for Assignment 7

Created by Michael Henson on 27 Jan 2016.
Copyright 2016 Michael W Henson. All rights reserved.

"""
import argparse
import re


def woo(x):
    '''
I got a lot of help from these places:
http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
https://docs.python.org/2/library/string.html
http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
    '''
#removing whitespace
    x = str(x.replace(" ", ""))
    x = str.lower(x)
    x = re.sub(r'[^\w\s]','',x)
    return x


def wooing(x):
#reversing the cleaned data
    x = woo(x)
    y = x[::-1]
    return y


def checker():
        x = userdefined()
        if woo(x) == wooing(x):
            return "Way to Go! Its a palindrome"
        else:
            return "Sorry try again"


def userdefined():
    parser = argparse.ArgumentParser()
    parser.add_argument("palindrome", help="Give me a Palidrome", type=str)
    args = parser.parse_args()
    return args.palindrome


def main():
    x = checker()
    print(x)

if __name__ == '__main__':
        main()
