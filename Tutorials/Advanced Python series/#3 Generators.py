import sys
def myGen_(num: int):
    res = 1
    while 1:
        res+=5
        yield res
        

val = myGen_(10_000)
for i in range(100):
    print(next(val))
    
print(sys.getsizeof(val))