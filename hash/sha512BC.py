
import hashlib

def blockchin(word, zeros=3):
    for number in range(0,1_000_000_000):
        hashBuffer = hashlib.sha3_512(bytes(word + "{}".format(number), "utf-8")).hexdigest()
        if hashBuffer[:zeros] == zeros * "0": break
        print(hashBuffer)
    return "Match : " + hashBuffer + "\nCheck : {}".format(number)

print(blockchin(input("Word : "), int(input("Number Of Zeros : "))))
