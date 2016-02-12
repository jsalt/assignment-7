# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 08:12:14 2016

@author: Glaucia
"""

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""


def sequence_eater(sequence, position):
    """prints all the values in a sequence, one at a time, in a different line"""
    #I included a condition, so we can control how many recursions will be made
    #As long as the position is smaller than the number of nucleotides in the sequence, the function will be called again
    if position < len(sequence):   
        print(sequence[position])
        #I replaced - by +, since we want to print the next value in the sequence, not the previous
        position += 1
        #With position reset for the next value in the string, we can call the function again
        sequence_eater(sequence, position)
    #if the position is bigger than the size of the string, nothing will be done and recursions stop.
    else:
        pass
    
def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)

if __name__ == '__main__':
    main()
    
