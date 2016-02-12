# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 21:37:41 2016

@author: Marco
"""

#!/usr/bin/env python
# encoding: utf-8

"""
fix_me.py

Created by Brant Faircloth on 03 February 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.
"""

###Fixed###

def sequence_eater(sequence, position):
    '''
    This recursive function prints each base of a given sequence, 
    one base per line 
    '''    
    # I used a Try - Except statement to control the recursion    
    try:    
        print(sequence[position])
        # I changed "-" to "+"
        position += 1
        sequence_eater(sequence, position)
    except:
        pass

def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence, 0)


if __name__ == '__main__':
    main()