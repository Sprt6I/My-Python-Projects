class SpecStr():
  def __init__(self, string: str):
    self.string = string
    
  def EndWith_(self, suffix: str) -> bool:
    return self.string[-len(suffix):]==suffix
  
  def SwapCase_(self) -> str:
    return ''.join([letter.lower() if letter.upper()==letter else letter.upper() for letter in self.string])
  
  def ZFill_(self, letter: str, numOfLetter: int, start=True) -> str:
    if start:return letter*numOfLetter+self.string
    return self.string+letter*numOfLetter  
  
  def Title_(self) -> str:
    spec = True
    s = ''
    
    for letter in self.string:
      if spec==True:
        s+=letter.upper()
        spec = False
      else:
        if letter==' ':
          spec = True
        s+=letter.lower()
        
    return s
  
  def IsLower(self) -> bool:
    for letter in self.string:
      if letter.lower()!=letter: return False
    return True

  def IsUpper(self) -> bool:
    for letter in self.string:
      if letter.upper()!=letter: return False
    return True

  def IsSpace(self) -> bool:
    for letter in self.string:
      if letter!=' ': return False
    return True

  def Capitalize_(self) -> str:
    return self.string[0].upper()+self.string[1:].lower()
  
  def ReverseString_(self):
    return self.string[::-1]

  def CountLetter_(self, letter: str) -> int:
    return sum([1 for i in self.string if i==letter])

  def IsAlNum_(self) -> bool:
    for letter in self.string:
      if letter not in '1234567890': return False
    return True
  
  def MySplit_(self, char: str) -> list[str]:
    ret = []
    poi = 0
    s = ''
    
    while poi<len(self.string):
      if self.string[poi]==char:
        ret.append(s)
        s = ''
      else:
        s+=self.string[poi]
      poi+=1
      
    ret.append(s)
    
    return ret
  
  def ChangeLet_(self, fromS: str, toS: str) -> str:
    return ''.join([i if i!=fromS else toS for i in self.string])



  def FindLetter_(self, letter: str) -> int:
    """Finds Letter In Sring

    Args:
        string (str): String To Find Letter
        letter (str): Letter To Find

    Returns:
        int: Position Of Letter In String
    """
    for indx, val in enumerate(self.string):
      if val==letter: return indx
    return -1
    
  
s = SpecStr('hehe')
print(s.EndWith_('he111'))