import random as rd


def generatorPass (key) :
    try : 
        key,a,b =key[0],int(key[1]),int(key[2])
        if a<b :
            print("lenght will keep default 4,6")
            a,b = 4,6
    except :
        key,a,b = key[0],4,6

        
   

    password = ""

    key = key.lower()
    key += key.upper()
    key += "0123456789"
    lenght = rd.randint(a,b)
    for  i in range(lenght) :
        password += rd.choice(key)
    return password




if __name__ == "__main__":
    user_input = input("Please Enter key, length of pass min-max seperated by comma\n (example:key,3,8)\n:").strip()
    user_key = [items for items in user_input.split(",")]
    print(user_key)
    loopCounter = 100
    for i in range (loopCounter) : 
        print(generatorPass(user_key))
    
    

