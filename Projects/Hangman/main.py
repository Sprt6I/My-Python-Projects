def Game_():
    maxNumOfTries = 7
    numberOfTries = 0
    
    wordToGuess = input("Input Word To Guess: ")
    if len(wordToGuess)<2:
        return -1
    
    
    guessingWord = '_'*len(wordToGuess)
    
    while maxNumOfTries>0:
        print('\n\n')
        guessedChar = input('Guess Letter: ')
        if len(guessedChar)>1 or guessedChar==None or guessedChar=='':
            print('Must be 1 char')
            continue
        
        guessingWord = [a for a in guessingWord]
        print(guessedChar)
        print(wordToGuess)
        if guessedChar in wordToGuess:
            for i,_ in enumerate(wordToGuess):
                if guessedChar==_:
                    print(_)
                    guessingWord[i]=_
        else:
            maxNumOfTries-=1
                
                
        guessingWord = ''.join(guessingWord)        
        print(guessingWord)
        
        if '_' not in guessingWord:
            print('U Won !!!')
            return 0

    print('U Lost :/')
    return 0

Game_()
        
    
    