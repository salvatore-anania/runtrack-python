def long(list):
    count=0
    for i in list:
        count+=1
    return count

def add(L,x):
    L+=[x]


def croissant(list):
    copielist=[]
    trie=[]
    max=list[0]
    min=list[0]
    ignore=min
    ignoreind=0
    for y in range(long(list)):
        add(copielist,list[y])
        if list[y]>max:
                max=list[y]               
    for y in range(long(list)):
        for i in range(long(list)):
            if copielist[i]<min and copielist[i]!=ignore:
                min=copielist[i]
                ignoreind=i
                if y==0:
                    ignore=min
        copielist[ignoreind]=ignore
        add(trie,min)
        min=max
    return trie

def arondi(L):
    for i in range(long(L)):
        temp=L[i]
        arrondi=0
        while temp>1:
            arrondi+=1
            temp-=1
        if temp<0.5:
            L[i]=arrondi
        elif temp>=0.5:
            L[i]=arrondi+1
    

L=[22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
arondi(L)
print(L)
print(croissant(L))