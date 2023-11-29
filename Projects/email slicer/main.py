def Gmail():
  inp = input('Input gmail: ')

  if '@' not in inp: return False
  if '.' not in inp: return False
  
  name = inp[:inp.index('@')]
  domain = inp[inp.index('@')+1:inp.index('.')]
  dot = inp[inp.index('.')+1:]
  
  if not name: return False
  if not domain: return False
  if not dot: return False
  
  
  print(f'Name: {name}')
  print(f'Domain: {domain}')
  print(f'Dot: {dot}')
  return 1

Gmail()
  
  
    