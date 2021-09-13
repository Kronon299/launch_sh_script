import threading, time, random
from queue import Queue

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
    if FUZZ:
        time.sleep(random.random())


###########################################################################################
q = Queue(1)
counter = 0
q.put(counter)


def worker(qu):
    'My job is to increment the counter and print the current count'
    global counter
    oldcnt = qu.get()
    fuzz()
    fuzz()
    counter = oldcnt + 1
    fuzz()
    print('The count is %d' % counter, end='')
    fuzz()
    print()
    fuzz()
    print('---------------', end='')
    fuzz()
    print()
    fuzz()
    qu.put(counter)
    qu.task_done()


print('Starting up')
fuzz()
for i in range(10):
    threading.Thread(target=worker, args=(q,)).start()
    fuzz()
q.get()
# q.join()
print('Finishing up')
fuzz()
