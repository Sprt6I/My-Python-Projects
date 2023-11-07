import threading

def myfunc1_(rangee:int):
    for i in range(rangee):
        print('\nhehe')
        
def myfunc2_(rangee: int):
    for i in range(rangee):
        print('\nhi')
        
threadMyFunc1 = threading.Thread(target=myfunc1_, args=(10,))
threadMyFunc2 = threading.Thread(target=myfunc2_, args=(10,))

threadMyFunc1.start()
threadMyFunc2.start()

threadMyFunc2.join()

print('Script Ended')

