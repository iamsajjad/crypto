
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

