import sys

def calculpoid(mot):
    pond=1
    poid=0
    for j in range(len(mot)-1,-1,-1):
            poid+=(ord(mot[j])-96)*pond
            pond*=10
    return poid
            
str="abbbbba"
test=list(str)
plusproche=sys.maxsize
poidmot=calculpoid(str)
for lettermove in range(len(str)):
    del test[lettermove]
    for motdif in range(len(test)+1):
        test.insert(motdif,str[lettermove])
        poidnew=calculpoid(test)
        proximite=poidnew-poidmot
        if poidnew>poidmot and proximite<plusproche and proximite!=0 :
            motproche=''.join(test)
            plusproche=proximite
        del test[motdif]
    test.insert(lettermove,str[lettermove])
print(motproche)