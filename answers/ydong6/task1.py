'''
Created on Feb 9, 2016

@author: Yuankai
'''

def palindrome(a):
    a=input('Enter :')
    b=a[::-1]
    if a==b:
        print ("yes,this is palindrome.")
        return True
        
    else:
        print("no, its not a palindrome.")
        return False 
        

def main():
    a=1
    palindrome(a)
   
if __name__ == '__main__':
    main()
    