#! /usr/bin/env python
# encoding: utf-8

'''
Assignment 7 Task 1
Write a generalized program proving something is a
palindrome or not. Take input using the argparse module.
'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("pd", type=str)
args = parser.parse_args()


def pd(args):
    a = str() == str()[::-1]
    if a is True:
        print("That's a palindrome!")
    if a is False:
        print("Nope not a palindrome.")


def main():
    pd(args)


if __name__ == '__main__':
    main()
