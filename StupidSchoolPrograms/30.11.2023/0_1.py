try:
  m = int(input("Input length:"))
  n = int(input("Input number of rows: "))
except:
  print('Wrong Input')
  exit()
  
for ns in range(n):
  s = ''
  for ms in range(m):
    s+='1' if ns%2==0 else '0'
  print(s)
