# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 07:49:03 2016

@author: Glaucia
"""
"""

Task 1

"able was i ere i saw elba" is a well-known palindrome. Write a generalized program 
that proves this phrase is a palindrome. Because the program is generalized, it should 
also prove that any other palindromes are actually palindromes and it should prove when 
phrases or words are not palindromes. Be sure to write your program such that this is the case. 
And, be sure that your argument takes any palindrome on the command line as input 
(i.e., use the argparse module). Write the program to include a main() function and the 
ifmain statement. The main() function should call the function or functions that you create 
to test for "palindrome-ness".

"""
import argparse

def testpalindrome(string):
    """tests if a string is a palindrome, it accpets words and phrases with white spaces
    ! ? ; : , and . """
    #this takes the white spaces and other characters out of the provided string
    string=string.replace("!","")
    string=string.replace("?","")
    string=string.replace(";","")
    string=string.replace(":","")
    string=string.replace(".","")    
    string=string.replace(",","")
    string=string.replace(" ","")
    #this tests if the reverse of string is the same as the forward
    if string == string[::-1]:
        #and returns a boolean value
        return True
    else:
        return False

def arginput():
    #creating a Argument Parser object and storing it in the parse variable
    parse = argparse.ArgumentParser()
    #this is going to tell the user to add the maximum argument in the comand prompt
    parse.add_argument("string", help="type a word or expression using lower case letters",type=str)
    #getting the string provided by the user and transforming in an object for my function   
    args = parse.parse_args()
    #this is going to run my function, as soon as the user provide a string to be tested in terms of "palindome-ness"    
    result=testpalindrome(args.string)
    print(result)
    
def main():
    arginput()

if __name__ == "__main__":
    main()