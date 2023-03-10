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
    
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(croissant(L))