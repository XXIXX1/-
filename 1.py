import sys 

def getA(n):
    x=0
    for i in range(n):
        x+=1
    return x / len(n) 
    
def getM(n):
    for i in range(n):
        for j in range(n):
            if n[i]<n[j]:
                x=n[i]
                n[i]=n[j]
                n[j]=x
    z=int(len(n)/2)
    return n[z]

if __name__=="__main__":
    if len(sys.argv)>1:
        n=list(map(int,sys.arge[1:]))
        print("AVG:{}".format(getA(n)))
        print("MID:{}".format(getM(n)))
