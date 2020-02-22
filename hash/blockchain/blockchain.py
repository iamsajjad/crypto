
import time
import hashlib
import subprocess
from threading import Thread
from queue import Queue

"""

import sys
import hashlib

def subbandthread(word, zeros, start, end):
    for number in range(start, end):

        hashBuffer = hashlib.sha3_512(bytes(word + "{}".format(number), "utf-8")).hexdigest()
        if hashBuffer[:zeros] == zeros * "0": break
        print(hashBuffer)
    return "\nMatch : " + hashBuffer + "\nCheck : {}\n".format(number)

out = subbandthread(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))

with open('result.txt', '+a') as result:
    result.write(out)
"""

class BlockChain:

    def __init__(self, word, zeros=3, threads=128, rangeOfBandes=1_000_000_000):
        self.word = word
        self.zeros = zeros
        self.threads = threads
        self.rangeOfBandes = rangeOfBandes

    def router(self, thread, queue, word, zeros, log=True):
        
        """
        Threads Make
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

    @property
    def run(self):

        queue = Queue()

        bandes = []
        band = self.rangeOfBandes // self.threads
        subband = self.rangeOfBandes // self.threads
        for i in range(self.threads):
            bandes.append((band-subband, band))
            band += subband

        for thread in range(self.threads):
            subRange=bandes[thread]
            worker = Thread(target=self.router, args=(thread, queue, self.word, self.zeros))
            worker.setDaemon(True)
            worker.start()

        #print(bandes)

        for band in bandes:
            queue.put(band)
        queue.join()

# Example
print(BlockChain("a", 4, 512).run)
