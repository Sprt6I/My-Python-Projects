import random
def Encypt():
    text = input('Input text to encrypt: ')
    text = [_ for _ in text]
    Keyarr = []
    for i, _ in enumerate(text):
        randToAdd = random.randrange(1200, 10000) #Number To Add
        randLeft = random.randrange(0, 6) #Number Of Numbers To Add From Left
        randRight = random.randrange(0, 6) #Number Of Numbers To Add From Right
        text[i] = ''.join([f'{_}{random.randrange(9)}' for _ in str(int(ord(_))+randToAdd)]) #Changes char (np H) to ascii H->72 then adds randToAdd to it
            
        for a in range(randLeft): #Adds randLeft numbers from left (at start)
            text[i] = f'{random.randrange(9)}' + text[i]
             
        for a in range(randRight): #Adds randRight numbers from rigth (at end)
            text[i] += f'{random.randrange(9)}'
            
        Keyarr.append([randLeft, randToAdd, randRight])
    text = '/'.join(text)

    #print(f'Added Arr: {Keyarr}')
    print('\n\n\nEncrypted:\n')
    print(f'{text}')
    Decode(text, Keyarr)
    return text

def Decode(text, key):
    print('\n\n\nDecrypted:\n')
    text = text.split('/')
    #print(text)
    for i, _ in enumerate(text):
        if key[i][2]:
            text[i] = chr(int(_[key[i][0]:-key[i][2]-1:2])-key[i][1]) #cuts randLeft number from start and randRight from end. And pass every secound digit.Then substracts randToAdd from number
        else:
            text[i] = chr(int(_[key[i][0]:-1:2])-key[i][1]) #doest the same but when randRight==0
    print(''.join(text))
    
    return 0
   
Encypt()
