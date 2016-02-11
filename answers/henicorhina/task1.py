# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 7
Oscar Johnson 10 February 2016
"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(
            description=""" test a string for whether it is a palindrome  """
        )
    parser.add_argument('--string',
                        dest = "string",
                        required = True,
                        type = str,
                        help = "enter a string of characters to test whether it is a palindrome"
                        )
    return parser.parse_args()


def palindrome(args):
    """
    function takes a string and proves whether or not 
    it is a palindrome
    """
    args.string = args.string.replace(" ", "") # removes whitespace
    if args.string[::-1] == args.string: 
        #reverses strings and compares if they are equal
        #print (string)        
        return "this is a palindrome"

    elif args.string[::-1] != args.string:
        #reverses strings and compares if they are not equal
        #print (string)        
        return "this is not a palindrome"
    
    else:
        return "you have failed somehow"
        

def main():
    #x = str(input ("what is your palindrome? "))
    args = get_args()
    print (palindrome(args))


if __name__ == '__main__':
    main()

