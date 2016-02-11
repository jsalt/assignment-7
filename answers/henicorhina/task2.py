# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 6
Oscar Johnson 9 February 2016
"""
## Task 2

"""
Here is a recursive program that is mean to print each base of a given 
input sequence to the screen, one base per line.
"""

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""



def sequence_eater(sequence, position):
    if position == len(sequence):
        # recursive function was missing a base case
        return 0
    else:
        print(sequence[position])
        #print (position)
        position += 1
        sequence_eater(sequence, position)


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()


