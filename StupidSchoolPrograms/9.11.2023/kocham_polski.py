# Zad. 2 Program wyświetlający w kolejnych wierszach n napisów Lubię język polski [kocham_polski.py]
try:num = int(input('input how many times u want to write it: '))
except:
    print('Wrong Input')
    exit()
    
for i in range(num):
    print('Lubię język polski')