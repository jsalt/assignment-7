#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

BIOL7800 Assignment 7 Task 2

Amie Settlecowski
11 Feb. 2016

Edited version of fix_me.py, copyright 2016 Brant Faircloth.
"""


def sequence_eater(sequence, position):
    if position < len(sequence):
        # print(position)
        print(sequence[position])
        position += 1
        sequence_eater(sequence, position)


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()
