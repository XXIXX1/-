import sys
import random

if __name__=="__main__":
    if len(sys.argv) >2:
        seedValu=int(sys.argv[1])
        data=list(sys.argv[2])
        random.seed(seedValu)
        random.shuffle(data)
        print("".join(data))
