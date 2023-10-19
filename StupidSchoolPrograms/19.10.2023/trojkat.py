num1 = float(input("Input 1 Number: "))
num2 = float(input("Input 2 Number: "))
num3 = float(input("Input 3 Number: "))



if num1**2+num2**2==num3**2 or num1**2+num3**2==num2**2 or num2**2+num3**2==num1**2:
    print("True")
else:
    print("False")
