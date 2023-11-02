try:
    num1 = float(input('Input num1: '))
    num2 = float(input('Input num2: '))
except:
    print('Input numbers !!!')
    exit()

if num1>num2:print('num1 is bigger')
elif num2>num1: print('num2 is bigger')
else: print('nums are equal')