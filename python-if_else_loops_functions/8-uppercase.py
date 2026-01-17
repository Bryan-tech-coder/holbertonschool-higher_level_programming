#!/usr/bin/python3
def uppercase(str):
    chaine = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            chaine += chr(ord(str[i]) - 32)
        else:
            chaine += str[i]
    print("{}".format(chaine))
