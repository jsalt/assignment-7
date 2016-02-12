'''
Created on Feb 9, 2016

@author: Yuankai
'''

def sequence_eater(sequence, position):
    if position<=23:
        print(sequence[position])
        position += 1
        #print(position)
        sequence_eater(sequence, position)
    else: 
        print("done")


def main():
    sequence = "ATCGCGTAGCACGACTCTGCTCGC"
    sequence_eater(sequence,0)
    #print("yet")


if __name__ == '__main__':
    main()