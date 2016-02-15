#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.

Fixed by: Austen T. Webber 2016_2_11
"""


def sequence_eater(sequence, position):
    if position<len(sequence):
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


# https://docs.python.org/2/library/stdtypes.html
