import os 

fname = input('Please Enter File: ')

if len(fname) < 1 : fname = 'clown.txt'
hand = open (fname)
di = dict()
for i in hand :
    lim = i.rstrip()
    # print(lim)
    wds = lim.split()
    # print(wds)
    for w in wds :
        # print(w)
        # if w in di :
        #     di[w] = di[w] + 1
        #     print('***existing...')
        # else :
        #     di[w] = 1
        #     print('**** New')
        # print(di[w])
        # ----- Second Method ------
        # Dictionary Method -------



        # ----
        # di.get(w,0) if w not exist return  0
        # so oldCount = 0
        # ----

        # oldCount = di.get(w,0)
        # print(w,'Old',oldCount)
        # newCount = oldCount + 1
        # di[w] = newCount
        # print(w,"New",newCount)
        #               Make all of them only line
        di[w] = di.get(w,0) + 1
        # print(w,'New',di[w])
# print(di)
#  Which Word Largest has frequency
largest = -1
key = None
for  k,v in di.items():
    print(k,v)
    if v > largest :
        largest = v
        key = k
print('----------')    
print("Done",largest,"Key--:",key)