#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py is a recursive program that is meant to print each base of a given
input sequence to the screen, one base per line.

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.

Corrected by Shraddha Shrestha on 8th February 2016.

"""


def sequence_eater(sequence, position):
    #position cannot be more than the sequence length, so the recursion limit
    #is the length of sequence.
    position_limit = len(sequence)
    if position > position_limit:
        return 0
    elif position < position_limit:
        print(sequence[position])
        position+=1 #position-=1 gives a different result, hence changed to +=
        sequence_eater(sequence, position) #here is the recursion part
    else:
        return 0


def main():
    sequence="ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()
