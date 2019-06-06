from multiprocessing import Queue
from threading import Thread
import time

def producer(d):
    print ('start pruducer')
    for i in range(10):
        d.put(i)
        print ('producer to put:',i)
        time.sleep(0.5)

def customer(d):
    print ('start customer')
    while 1:
        data = d.get()
        print ('customer get msg:',data)

if __name__ == "__main__":
    q = Queue()
    pro = Thread(target=producer,args=(q,))
    prw = Thread(target=customer,args=(q,))
    pro.start()
    prw.start()