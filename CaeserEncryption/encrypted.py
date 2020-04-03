import math


def encrypted (text, value):
    output = ''
    for char in text :
        
        output += chr(ord(char)+value)
    return output





if __name__ == "__main__":
    print('\t '+"*"*30)
    print('''
                        Welcome 
                Encrypted your text 
                by Caesar Encryption
            ''')
    print('\t '+"*"*30)
    print("""
    1- Encryption
    2- Decryption
    """)
    try :
        clicked = int(input("Please Enter 1 or 2 :"))
    except ValueError :
        print('Please Enter just 1 or 2 ')
        
    

    value = abs(int(input("Please enter number of value Encryption:")))
    user_text = input("Please enter text: ")
    if clicked == 1 :
        print(encrypted(user_text,value))
    elif clicked == 2 : print(encrypted(user_text,(value*-1)))
    else : 
        print('Menu options 1 or 2 exist please clicked 1 or 2 : Default Mode  = 1')
        print(encrypted(user_text,value))
    

    
        


    
    