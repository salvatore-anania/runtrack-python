def long(list):
    count=0
    for i in list:
        count+=1
    return count


def add(L,x):
    L+=[x]

def separation(str):
    phrase = []
    mot = ""
    for i in str:
        if i != " ":
            mot += i
        else:
            add(phrase,mot)
            mot = ""
    return phrase

def my_long_word(n,str):
    mots = separation(str)
    phrasePlus3 = ""
    for i in mots:
        if long(i) > n:
            phrasePlus3 += i
            phrasePlus3 += " "
    return phrasePlus3

print(my_long_word(3," La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"))