#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.

Task2 of assignment 7. Editing Brant C. Faircloths Fix_me.py
"""


def sequence_eater(sequence, position):
    '''
    At first this was weird, but once I saw why to use en vs.
    len and then got some help on why - vs + it made a lot more sequence
    Here are some good help sites I used for this:
    http://stackoverflow.com/questions/14886881/unorderable-types-int-str
    https://docs.python.org/3/library/functions.html#int
    http://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
    http://stackoverflow.com/questions/2932511/letter-count-on-a-string
    '''
    if position < len(sequence):
#you need this statement so that you are walking each base
        print(sequence[position])
        position += 1
#I believe the + allows you to walk forward rather then the -
#that walks you backwards and cause the loop to be continuous
        sequence_eater(sequence, position)
    else:
        pass


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()
