import sys
str="abbbbba"
liste=list(str)
test=list(str)
poidmot=0
pond=1
proche=0
motproche=''
plusproche=sys.maxsize
for h in range(len(str)-1,-1,-1):
    poidmot+=(ord(test[h])-96)*pond
    pond*=10
for mouv in range(len(str)):
    del test[mouv]
    for motdif in range(len(test)+1):
        poidnew=0
        pond=1
        test.insert(motdif,str[mouv])
        for j in range(len(test)-1,-1,-1):
            poidnew+=(ord(test[j])-96)*pond
            pond*=10
        proche=poidnew-poidmot
        if poidnew>poidmot and proche<plusproche and poidnew-poidmot!=0 :
            motproche=''.join(test)
            plusproche=proche
        del test[motdif]
    test.insert(mouv,str[mouv])
print(motproche)