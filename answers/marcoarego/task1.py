# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:53:06 2016

@author: Marco
"""

'''

Task 1

"able was i ere i saw elba" is a well-known palindrome. Write a generalized 
program that proves this phrase is a palindrome. Because the program is 
generalized, it should also prove that any other palindromes are actually 
palindromes and it should prove when phrases or words are not palindromes. 
Be sure to write your program such that this is the case. And, be sure that 
your argument takes any palindrome on the command line as input (i.e., use the
argparse module). Write the program to include a main() function and the 
ifmain statement. The main() function should call the function or functions 
that you create to test for "palindrome-ness".

'''

import argparse

def palindrome(string):
    """
    Function that test if any word of phrase is a palindrome
    """
    string = string.lower().replace(" ","")
    if string == string[::-1]:
        return True
    else:
        return False


def main():
    """ 
    Main function that calls the palindrome function.
    """
    parser = argparse.ArgumentParser()
    
    # Adding an argument to 'parse'
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose",action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("string",
                       help= "Please insert a string between quotes" 
                       " after the function name" ,
                       type=str)
    #parser.add_argument("-o","--output", help="output result to a file\n",
     #                   action="store_true")
                            
    args = parser.parse_args()
    
    result = palindrome(args.string)
    if args.verbose:
        print("The string " +str(args.string)+" is a palindrome")
    elif args.quiet:
        print(result)
    else:
        print("palindrome(" + str(args.string)+") = "+str(result))
    
    return result
    
if __name__ == '__main__':
    main()