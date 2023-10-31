from random import randrange, choice
import sys
sys.path.append('C:/Users/User/Documents/GitHub/Python')
from Bouble_Sort.BoubleSort import Sorting
tests = []

for _ in range(35):
    arr = Sorting.Bsort([randrange(0, 20000) for _ in range(500)])
    numToFind = choice(arr)
    tests.append({
        'input': {
            'arr': arr,
            'num': numToFind
        },
        'output': arr.index(numToFind)
    })
    
#print(tests)