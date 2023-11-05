# First I Want To State I Don't Understand Any Of This
'''
def myDecorator_(function):
    
    def header_(*args, **kwargs):
        print(args)
        print(kwargs)
        print(f'I Am Header !')
        function(*args, **kwargs)
        
    return header_

@myDecorator_
def notHelloWorld_(name: str):
    print(f'Not Hello {name[0].upper() + name[1:].lower()}')
    
notHelloWorld_('Not Me Plss')
'''

# Practical Example - Logging
'''
def  logged_(function):
    def wrapper(*args, **kwargs):
        value = function(*args, *kwargs)
        with open('#2 logfile.txt', 'a+') as file:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            file.write(f'{fname} returned value {value}')
        return value
    return wrapper

@logged_
def add_(x: int | float,y: int | float):
    return x+y

print(add_(5.4, 5))
'''
# I think I Understand When To Use it 😮 (I am amazing)


# Practical Example 2
import time

def timed_(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        fname = function.__name__
        after = time.time()
        print(f'{fname} took {after-before} secounds to execute')
        return value
    return wrapper
    
@timed_    
def myFunction_(num: int):
    return sum([i for i in range(num)])

print(myFunction_(1_000_000))