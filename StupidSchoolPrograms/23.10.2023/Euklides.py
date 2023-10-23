def euklides(num1:int, num2:int) -> int:
    if num1>num2:
        r=num1%num2
        while r>0:
            pastR = r
            r = num2%r
        return pastR
    elif num2>num1:
        r=num2%num1
        while r>0:
            pastR = r
            r = num2%r
        return pastR
    else:
        return -1
print(euklides(78,282))
        
    