import math
premier=False
for i in range(1,1001):
    for j in range(2,math.ceil(math.sqrt(i))+1):
        if i%j==0:
            premier=False
    if premier:
        print(i)
    premier=True