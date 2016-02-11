#!/usr/bin/env python
# utf-8

"""
TO REVIEWER!!!

I FAILED AT THIS TASK....



Created by Brant Faircloth on 03 February 2016.
Repaired by Jon Nations on 10 February 2016
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""

# Here is a recursive program that is mean to print each base of a given input
# sequence to the screen, one base per line.
# Alas, it is somewhat broken. Try to fix the program (while maintaining its
# function and its recursive nature) in the fewest number of changes possible.


def sequence_eater(sequence, position):
    print(sequence[position])
    position -= 1
    sequence_eater(sequence, position)


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()
