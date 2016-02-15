#!/usr/bin/env python
# encoding UTF-8

'''
Task2-a recursive program that is meant to print each base of a given input seq
to the screen, one base per line, which needs a bit of fixing...

#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""

def sequence_eater(sequence, position):
    print(sequence[position])
    position -= 1
    sequence_eater(sequence, position)

def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)

if __name__ == '__main__':
    main()

fix with the fewest steps possible...
'''


def sequence_eater(sequence, position):
    samt = len(sequence)
    if position < samt:
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
