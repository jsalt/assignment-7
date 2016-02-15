#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 7, Task 1
Austen T. Webber
2016_2_11
"""

import argparse
import re


# Remove whitespaces and punctuations
def palinput(x):
    x = str(x.replace(" ", ""))
    x = str.lower(x)
    x = re.sub(r'[^\w\s]','',x)
    return x


# Now to reverse that cleaned data
def revcheck(x):
    x = palinput(x)
    y = x[::-1]
    return y


# We need to test the input to see if it matches the reverse
def palicheck():
    x = palindrome()
    if palinput(x) == revcheck(x):
        return "TRUE plaindrome"
    else:
        return "FALSE not a palindrome"


# We need the user to actually input the potential palindrome
def palindrome():
    parser = argparse.ArgumentParser()
    parser.add_argument("palindrome",
        help = "Type potential palindrome in quotes after .py", type=str)
    args = parser.parse_args()
    return args.palindrome


def main():
    x = palicheck()
    print(x)


if __name__ == '__main__':
        main()


# https://docs.python.org/2/howto/argparse.html
# http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
# http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
