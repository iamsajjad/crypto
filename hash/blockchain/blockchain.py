
import time
import hashlib
import subprocess
from threading import Thread
from queue import Queue

"""
def subbandthread(start, end):
    for number in range(start, end):

        hashBuffer = hashlib.sha3_512(bytes(word + "{}".format(number), "utf-8")).hexdigest()
        if hashBuffer[:zeros] == zeros * "0": break
        print(hashBuffer)
    return "Match : " + hashBuffer + "\nCheck : {}".format(number)
"""

def pinger(thread, queue, word, zeros, log=True):
    
    """
    Pings subnet
    """
    
    while True:

        startband ,endband = queue.get()

        if log: print("{0} Thread <{1}>".format(time.ctime(), thread))

        band = queue.get()
        ret = subprocess.call("python subbandthread.py {} {} {} {}".format(word, zeros, startband, endband),
        shell=True,
        stdout=open('/dev/null', 'w'),
        stderr=subprocess.STDOUT)

        queue.task_done()

def runner(word, zeros=3, threads=128, rangeOfNumbers=1_000_000_000):

    queue = Queue()

    bandes = []
    band = rangeOfNumbers // threads
    subband = rangeOfNumbers // threads
    for i in range(threads):
        bandes.append((band-subband, band))
        band += subband

    for thread in range(threads):
        subRange=bandes[thread]
        worker = Thread(target=pinger, args=(thread, queue, word, zeros))
        worker.setDaemon(True)
        worker.start()

    print(bandes)

    for band in bandes:
        queue.put(band)
    queue.join()

#print(blockchin(input("Word : "), int(input("Number Of Zeros : "))))
print(runner("sajjad", 4))
