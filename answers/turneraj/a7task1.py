#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 7. 

 Created by A.J. Turner on February 9, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""
import argparse

def palindrome():
	"""This function passes args to palindrome() to see if a phrase is or is not a palindrome
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("palindrome", help="Checking to see if your imput is a palindrome. Please use quotes around the string you're checking.")
	args = parser.parse_args()
	answer = args.palindrome
	answer = answer.replace(" ","").lower()
	if str(answer) == str(answer)[::-1]: #check to for "palindromness"
		print ("Congrats, this is a palindrome!")
	else:
		print ("Sorry, this isn't a palindrome.")

		
def main():
	palindrome()
	
	
if __name__== '__main__':
	main()