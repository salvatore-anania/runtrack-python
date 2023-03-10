def decale(message, index):
    alpha="abcdefghijklmnopqrstuvwxyz"
    messag=list(message)
    notfind=True
    for i in range(len(messag)):
        for j in range(len(alpha)):
            if alpha[j]==messag[i] and notfind==True :
                notfind=False
                if j+index<27:
                    messag[i]=alpha[j+index]
                else:
                    messag[i]=alpha[(j+index)%26]
        notfind=True
    return ''.join(messag)

print(decale("test",1))