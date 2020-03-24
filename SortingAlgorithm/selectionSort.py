


def sorting (ar) :
    lenght = len(ar)
    
    
    for i in range(lenght-1) :
        if ar[i] > ar[i+1] : 
            ar[i], ar[i+1] = ar[i+1],a[i]

    return ar


a = [2,1,6,5,3,6,876,46,3453,2,1,0]
print(sorting(a))