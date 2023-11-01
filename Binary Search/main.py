import sys
from random import randrange
sys.path.append('C:/Users/User/Documents/GitHub/Python')
from Bouble_Sort.BoubleSort import Sorting
from BinarySearchTests import tests

def Binary(arr: list[int], num: int)-> list[int]:
    indx = len(arr)
    x = arr.copy()
    while len(arr)>1: #While more then 1 element in arr
        halfLen = int(len(arr)/2) #Get half of the array's len
        
        leftSide = arr[:halfLen] #Left half of array
        RightSide = arr[halfLen:] #Right half of the array
        
        if num in leftSide:#If number we look for is in left half of array: array = leftside of itself else rightside
            arr = leftSide
            indx -= len(RightSide)
        else:
            arr = RightSide
            #indx -= len(RightSide)
            
    #print([arr[0], indx-1])
    #print(f'Should: {x.index(num)}')
    #print(f'indx: {indx-1}')
    return indx-1 #Return number we look for

for _ in tests:
    print(Binary(**_['input']) == _['output'])
