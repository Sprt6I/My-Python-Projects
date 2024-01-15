def ChangeLet_(string:str, fromS: str, toS: str) -> str:
  return ''.join([i if i!=fromS else toS for i in string])



def FindLetter_(string: str, letter: str) -> int:
  """Finds Letter In Sring

  Args:
      string (str): String To Find Letter
      letter (str): Letter To Find

  Returns:
      int: Position Of Letter In String
  """
  for indx, val in enumerate(string):
    if val==letter: return indx
  return -1



def MySplit_(string: str, char: str) -> list[str]:
  """Splits String By Given character  (char)

  Args:
      string (str): String To Be Separeted
      char (str): Char To Separate By

  Returns:
      list[str]: Separeted Pieces Of String
  """
  ret = []
  poi = 0
  s = ''
  
  while poi<len(string):
    if string[poi]==char:
      ret.append(s)
      s = ''
    else:
      s+=string[poi]
    poi+=1
    
  ret.append(s)
  
  return ret



def MyJoin_(stringLst: list[str], connector:str) -> str:
  s = ''
  i = 0
  while i<len(stringLst)-1:
    if stringLst[i]:
      s+=stringLst[i]+connector
    i+=1
    
  s+=stringLst[i]
  
  return s


def ReverseString_(string: str):
  return string[::-1]

def CountLetter_(string: str, letter: str) -> int:
  return sum([1 for i in string if i==letter])

def IsAlNum_(string: str) -> bool:
  for letter in string:
    if letter not in '1234567890': return False
  return True

def IsLower(string: str) -> bool:
  for letter in string:
    if letter.lower()!=letter: return False
  return True

def IsUpper(string: str) -> bool:
  for letter in string:
    if letter.upper()!=letter: return False
  return True

def IsSpace(string: str) -> bool:
  for letter in string:
    if letter!=' ': return False
  return True

def Capitalize_(string: str) -> str:
  return string[0].upper()+string[1:].lower()

def Title_(string: str) -> str:
  spec = True
  s = ''
  
  for letter in string:
    if spec==True:
      s+=letter.upper()
      spec = False
    else:
      if letter==' ':
        spec = True
      s+=letter.lower()
      
  return s


def EndWith_(string: str, suffix: str) -> bool:
  return string[-len(suffix):]==suffix



def SwapCase_(string: str) -> str:
  return ''.join([letter.lower() if letter.upper()==letter else letter.upper() for letter in string])


def ZFill_(string: str, letter: str, numOfLetter: int, start=True) -> str:
  if start:return letter*numOfLetter+string
  return string+letter*numOfLetter  