# Zad. 1 program wprowadzajacy 10 liczb rzeczywistych z klawiatury i zapamietujacy je kokejno w zmiennej liczba [liczba.py]
s = ''

for i in range(10):
    num = input(f'Input {i} num: ')
    s+=num
    
print(s)