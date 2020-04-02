import random as rd

def generatorPass (name) :
    password = ""

    name = name.lower()
    name  += name.upper()
    name += "012345"
    lenght = rd.randint(6,10)
    for  i in range(lenght) :
        password += rd.choice(name)
    return password

name = input ("Please Enter Key of name :  ") 
for i in range (10) : 
    print(generatorPass(name))
