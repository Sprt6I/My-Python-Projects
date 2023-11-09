# Zad. 5 Prosty kalkulator wybór rodzaju obliczenia z wykorzystanie menu, aby po wprowadzeniu z klawiatury obliczał działanie na dwóch liczbach [kalkulator.py]
import math
try:
    num1 = float(input('Input num 1: '))
    operator = input('Input operator (| = sqrt, ^ = pow): ')
    num2 = float(input('Input num 2: '))
except:
    print('Wrong Input')
    exit()
    
if operator not in '-+*/|^':
    print('Wrong Input')
    exit()
    
if operator in '-+*/':
    print(eval(f'{num1}{operator}{num2}'))
else:
    if operator=='|':
        print(f'{math.sqrt(int(f"{int(num1)}{int(num2)}"))}')
    else:
        print(f'{num1**num2}')