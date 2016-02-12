#!/usr/bin/env python
# encoding: utf-8

"""
Modified fix_me.py (Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.).

Recursive program to print each base of a given input sequence to the screen.

Elisa Elizondo
11 Feb. 2016
"""


def sequence_eater(sequence, position):
    ##added if/else to provide an end to the recursion##
    if position >= len(sequence):
        pass
    else:
        print(sequence[position])
        ##reversed direction; counting up instead of counting down##
        position += 1
        sequence_eater(sequence, position)


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()
