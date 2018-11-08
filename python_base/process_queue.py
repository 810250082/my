from multiprocessing import Process , queues

import os ,random , time

def p_write(q):
    print('%s start write:') % os.getpid()
    cont = ['A' , 'B' , 'C' , 'D']
    for i in cont:
        print("%s put %s" % (os.getpid() , i))
        q.put(i)
        time.sleep(random.random() * 3)

def p_read(q):
    print('%s start read:') % os.getpid()
    while True:
        cont = q.get(True)
        print('%s get %s' % (os.getpid() , cont))




if __name__ == "__main__":
    print('parent %s start work.' % os.getpid())

    q = queues.Queue()
    write = Process(target=p_write , args=(q , ))
    read = Process(target=p_read , args=(q , ))

    write.start()
    read.start()

    write.join()
    read.terminate()
    print('game over')
