import os 

fname = input('Please Enter File: ')

if len(fname) < 1 : fname = 'clown.txt'
hand = open (fname)

for i in hand :
    lim = i.rstrip()
    # print(lim)
    wds = lim.split()
    # print(wds)
    for word in wds :
        print(word)