 
import threading
import time
 
def deamon_task():
    print('Deamon thread is working')
    time.sleep(2)
 
def non_deamontask():
    print('nonDeamon thread is working')
    time.sleep(2)
    print('nonDeamon thread finished')
 
dt=threading.Thread(target=deamon_task())
dt.daemon=True
 
nt=threading.Thread(target=non_deamontask)
nt.start()
 
print('Main program exit')