import string
import random

def gen():
    s1 = string.ascii_uppercase
     
    s2= string.ascii_lowercase
     
    s3 = string.digits
    
    s4 = string.punctuation

    passlen = int(input("Enter the password Length\n"))

    s=[]
    #In Python, the extend() method, used with lists, adds all elements from an iterable (like another list, tuple, or string) to the end of the existing list, effectively merging the iterable into the original list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)

     
 
gen()