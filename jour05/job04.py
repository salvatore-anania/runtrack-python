def decale(message, index):
    alpha="abcdefghijklmnopqrstuvwxyz"
    messag=list(message)
    find=False
    for i in range(len(messag)):
        for j in range(len(alpha)):
            if alpha[j]==messag[i] and not find :
                find=True
                if j+index<26:
                    messag[i]=alpha[j+index]
                else:
                    messag[i]=alpha[(j+index)%26]
        find=False
    return ''.join(messag)

print(decale("test",8))