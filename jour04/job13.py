def add(L,x):
    L+=[x]

L= [10,20,30,20,10,50,60,40,80,50,40]
Lno2=[]
nodouble=True
for element in L:
    for elementNo2 in Lno2:
        if elementNo2 == element:
            nodouble=False
    if nodouble:
        add(Lno2,element)
    nodouble=True
print(Lno2)