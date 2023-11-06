'''
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    
func('hi', 'hello', abc='1', cba='2')
'''
import sys
if len(sys.argv)!=3:
    raise TypeError('Not enough arguments')

num1 = sys.argv[1]
num2 = sys.argv[2]
print(num1, num2)
def abc(x: int | float, y: int |float) -> int | float:
    return x*y

print(abc(int(num1),int(num2)))