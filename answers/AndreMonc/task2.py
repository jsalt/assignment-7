# !/usr/bin/env python
# encoding: utf-8

"""
Fixed version of Brant's program.
Created by Andre Moncrieff on 9 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
Original program created by Brant Faircloth on 03 February 2016.

This is a recursive program that prints each base of a given input sequence 
to the screen, one base per line.
"""


def sequence_eater(sequence, position):
    if position <= len(sequence) - 1:    
        print(sequence[position])
        position += 1
        sequence_eater(sequence, position)
    else:
        pass


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()