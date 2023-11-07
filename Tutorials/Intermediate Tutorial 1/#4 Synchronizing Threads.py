import threading
import time

num = 2
lock = threading.Lock()

def double_():
    global num, lock
    lock.acquire()
    while num<4096:
        num*=2
        print(num)
        time.sleep(1)
    lock.release()
        
def half_():
    global num, lock
    lock.acquire()
    while num>1:
        num/=2
        print(num)
        time.sleep(1)
    lock.release()
        
threadDouble = threading.Thread(target=double_)
threadHalf = threading.Thread(target=half_)

threadDouble.start()
threadHalf.start()

threadHalf.join()

print('Program Ended')
        
        