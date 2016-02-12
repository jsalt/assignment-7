#!/usr/bin/env python
# encoding: utf-8
"""
script for palindrome.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import argparse


def is_palindrome(word):
    word_rev = reversed(word)
    if list(word) == list(word_rev):
        return True
    else:
        return False


def main():
        parse = argparse.ArgumentParser()
        parse.add_argument("test_seq", help="type the" +
                           " sequence you need to test.", type=str)
        args = parse.parse_args()
        result = is_palindrome(args.test_seq)

        print(str(result))

if __name__ == '__main__':
    main()
