from multiprocessing import Pool
import os , time , random

def process_run(name):
    print "sub_process %s(%s) start run" % (name , os.getpid())
    startTime = time.time()
    time.sleep(random.random() * 3)
    endTime = time.time()
    print "process %s(%s) run %s second" % (name , os.getpid() , endTime - startTime)

if __name__ == "__main__":
    print "parent process %s start run" % os.getpid()
    pool = Pool(12)
    for i in range(13):
        pool.apply_async(process_run , args = (i ,))
    time.sleep(1)
    print "process %s start wait process end ..." % os.getpid()
    pool.close()
    pool.join()
    print "all process end."