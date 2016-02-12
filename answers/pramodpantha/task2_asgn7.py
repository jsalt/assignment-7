#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""


def sequence_eater(sequence, position):
    you_can_fix_me = len(sequence)
    if position < you_can_fix_me:
        print(sequence[position])
        position += 1
        sequence_eater(sequence, position)
    else:
        return 0


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)

if __name__ == '__main__':
    main()
