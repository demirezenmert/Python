import os

def say (w) :
    
    os.system('say {}'.format(w))
    return w



say("merhaba! isminiz nedir")
name = input(":")
age = input(say("Merhaba {}, yaşını bana söylermisin? :".format(name)))