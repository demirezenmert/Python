#insertionSort 

'''
    Insertion Sorting Algortihm

'''
def insertionSort (collection):
    
    length = len(collection)

    for i in range(1,length):
        insertion_index = i 
        while ( insertion_index > 0 
        and collection[insertion_index-1]> collection[insertion_index]
        ):
            collection[insertion_index-1],collection[insertion_index]=collection[insertion_index],collection[insertion_index-1]
            insertion_index -= 1
    return collection




if __name__ == "__main__":
    user_input = input("Please Enter numbers separated by comma(,):\n").strip()
    unsorted_collection = [int(items) for items in user_input.split(",")]
    print(insertionSort(unsorted_collection))

