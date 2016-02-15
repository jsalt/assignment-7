#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""


def sequence_eater(sequence, position):
    if position <= len(sequence)-1:
        print(sequence[position])
        position += 1  # here the position starts from count 0, so after 0 it should be 1 hence, (+) instead of (-).
        sequence_eater(sequence, position)
    else:
        return sequence  # this is the same as saying return None or making recursive to stop


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()
