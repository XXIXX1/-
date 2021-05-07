import numpy as np
import random

a=np.array([1,2,3,4])
#print(a)
b=np.array([(2.0,5,2,5.3),(2,6,9,8)], dtype=float)
#print(b)
c=np.array([[(2.0,5,2,5.3),(2,6,9,8)],[(5,8,7,9),(5,9,7,5)]], dtype=float)
#print(c)



x=np.ones((2,3,4))*128
y=np.full((2,3,4),128)
z=np.random.randint(1,100,(3,4))
k=z.reshape(1,12)

#print(x)
#print(y)
print(z)
print(k)

fileName="out2.npy"
with open(fileName,"wb") as fp:
    np.save(fp,y)