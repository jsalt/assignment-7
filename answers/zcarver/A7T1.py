#!/usr/bin/env python
# encoding UTF-8

'''
Task1-write a generalized program that proves or disproves this, "able was i
ere i saw elba", or any other phrase a palindrome. Using the 'argparse()'
module, be sure that the argument takes any palindrome on the command line as
inpute. This program should include ifmain and main().
'''

import argparse


def input_palind():
    parser = argparse.ArgumentParser(description='Enter str for validation.')
    parser.add_argument('palind', help="string to be tested for \
    palindrome", type=str)
    args = parser.parse_args()
    return args.palind


def str_p(IN):
    # reverse the string...
    rev_IN = reversed(IN)
    if IN == rev_IN:
        # check if the string is equal to its reverse
        print("It is palindrome")
        return IN
    else:
        print("It is not palindrome")


def main():
    input_palind()
    p = str_p()
    print(p)

if __name__ == '__main__':
    main()
