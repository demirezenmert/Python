#  Created by Mert Demirezen 
#  Copyright © 2019 Mert Demirezen. All rights reserved.


def selectionSorting(collection) :
    length = len(collection)

    for i in range(length-1):
        least = i
        for j in range(i+1,length):
            if collection[j] < collection[least] : least = j
        if least != i :
            collection[least],collection[i] = collection[i],collection[least]

    return collection






if __name__ == "__main__":
    user_array = input("Please Enter Number seperated by comma (,):").strip()
    unsorted = [int(item) for item in user_array.split(",")]
    print(selectionSorting(unsorted))