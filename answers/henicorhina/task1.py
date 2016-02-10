# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 7
Oscar Johnson 10 February 2016
"""


def palindrome(string):
    """
    function takes a string and proves whether or not 
    it is a palindrome
    """
    string = string.replace(" ", "") # removes whitespace
    if string[::-1] == string:
        #print (string)        
        return "this is a palindrome"

    elif string[::-1] != string:
        #print (string)        
        return "this is not a palindrome"
    
    else:
        return "you have failed somehow"
        

def main():
    x = str(input ("what is your palindrome? "))
    print (palindrome(x))


if __name__ == '__main__':
    main()

