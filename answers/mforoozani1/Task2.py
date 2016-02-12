#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""


def sequence_eater(sequence, position):
    print(sequence[position])
    a = len(sequence)
    if position == a-1:
        print()
    else:
        sequence_eater(sequence, position + 1)


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)

if __name__ == '__main__':
    main()
