import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def server_(numberOfThread: int):
    print(f'{numberOfThread} is trying to access')
    semaphore.acquire()
    print(f'{numberOfThread} connected')
    time.sleep(12)
    semaphore.release()
    print(f'{numberOfThread} disconnected')
    
for num in range(10):
    t1 = threading.Thread(target=server_, args=(num,))
    t1.start()
    time.sleep(1)
    