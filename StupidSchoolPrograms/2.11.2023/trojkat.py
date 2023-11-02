try:
    side1 = float(input("Input 1 side: "))
    side2 = float(input("Input 2 side: "))
    side3 = float(input("Input 3 side: "))
except: 
    print("Input numbers !!!")
    exit()
    
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print('Exists')
    print(f'obw: {side1+side2+side3}')
else:
    print('Does not exist')