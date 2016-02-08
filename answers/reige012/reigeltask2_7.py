#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py by Brant Faircloth was alterered by me in this program.  The alterations
I made were small and allowed the program to retain both its function and recursive
nature while eliminating all errors.

Edited by Alicia Reigel. 4 February 2016.
Copyright Alicia Reigel. Louisiana State University. 4 February 2016. All rights
reserved.

"""

def sequence_eater(sequence, position):
    """prints each letter of the sequence in order, each on a new line"""
    if position<len(sequence):
        #if the position is less than the lenght of the sequence do the following:
        print(sequence[position])
        position +=1
        #changed this to a +=1 to put the sequence letters in the correct order
        sequence_eater(sequence, position)
    else:
        #if the position is more than the sequence length do nothing.
        return 0


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)
    #eliminated a print statement here because it was printing nothing since there is no return statement in the above function



if __name__ == '__main__':
    main()
