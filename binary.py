
#
#
# n logn max arama sayisini 



def binarySearch (arr, elem):
    print(arr)
    if len(arr) == 1 :
        
        return arr[0] == elem
    if arr[len(arr) // 2] == elem :
        
        return True
    if arr[len(arr) // 2] > elem :
        
        return binarySearch(arr[:len(arr)//2],elem) 
    elif arr [len(arr) // 2] < elem :
        
        return binarySearch(arr[len(arr)//2:],elem) 
        
        
    
testArray = [1,4,5,4,3,5,634,45,5,3,1]

testArray.sort()

print(binarySearch(testArray,45))

