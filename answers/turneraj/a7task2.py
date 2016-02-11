#!/usr/bin/env python
# encoding: utf-8

"""
a7task2.py Created by A.J. Turner on 09 February 2016. This program modifies fix_me.py created by
Brant C Faircloth on 03 February 2016.
Copyright 2016 A.J. Turner. All rights reserved.

"""


def sequence_eater(sequence, position):
	print(sequence[position])
	position += 1 #changed from '-= 1' because it printed position zero followed by the rest of the 
	#sequence in reverse
	if position >= len(sequence):
		return #return with a black is needed to stop the recursive function at end of sequence
	else:
		sequence_eater(sequence, position) #recursive function singling out nucleotides within
		#a given sequence
	

def main():
	sequence = "ATCGCGTAGCACGACTCTGCTCGC"
	sequence_eater(sequence, 0)


if __name__ == '__main__':
	main()