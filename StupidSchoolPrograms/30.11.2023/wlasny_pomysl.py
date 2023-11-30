space = 8
star = 1
for i in range(5):
  print(''*space + '*'*star)
  star+=2
  space-=1
  
for i in range(6):
  print(''*space + '*'*star)
  star-=2
  space+=1