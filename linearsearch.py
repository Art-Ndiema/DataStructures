from array import *
pos=-1
def linsrch(a, x):
    #The linear search is difined
    i = 0
    #i is the index 
    while i < len(a):
        #im checking for i in the whole list a
        if a[i] == x:
            globals()['pos']=1
            #checking if i and x are a match
            return True
        i = i + 1
        #if x does not match we move to the next index till it found
    return False  


a = array('i', [18, 86, 80, 5, 43, 73, 28, 30, 55])
#this is my array (a)
x = 86
#86 is the element we are searching for
if linsrch(a, x):  
    print("Data found at:",pos+1)
    #output to show if x was found or not
else:
    print("Data not found")
