import random
def Encypt():
    text = input('Input text to encrypt: ')
    text = [_ for _ in text]
    Keyarr = []
    for i, _ in enumerate(text):
        randToAdd = random.randrange(1200, 10000)
        randLeft = random.randrange(0, 6)
        randRight = random.randrange(0, 6)
        #print(f'Without Added: {ord(_)}')
        #print(f'With Added: {int(ord(_))+randToAdd}')
        text[i] = ''.join([f'{_}{random.randrange(9)}' for _ in str(int(ord(_))+randToAdd)]) + f'{random.randrange(9)}'\
            
        for a in range(randLeft):
            text[i] = f'{random.randrange(9)}' + text[i]
            
        for a in range(randRight):
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
            text[i] = chr(int(_[key[i][0]:-key[i][2]-1:2])-key[i][1])
        else:
            text[i] = chr(int(_[key[i][0]:-1:2])-key[i][1])
    print(''.join(text))
    
    return 0
   
Encypt()
