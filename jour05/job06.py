def notes(list):
    for i in range(len(list)):
        if list[i]%5>=3 and list[i]>40:
            list[i]= list[i]+(5-list[i]%5)
    return list

list=[24, 41, 42, 43, 44]
print(notes(list))