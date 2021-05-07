import random

data=list("The is a book")
print("".join(data))
random.seed(1723)
random.shuffle(data)
print("".join(data))