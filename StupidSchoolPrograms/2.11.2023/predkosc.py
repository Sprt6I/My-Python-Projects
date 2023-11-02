try:
    road = float(input("Input road length km: "))
    time = float(input("Input number of hours: "))
except:
    print('Input numbers !!!')
    exit()
    
czas = road/time

if czas>90: print("Too fast")
elif czas==90: print("Ideal")
else: print('Too slow')