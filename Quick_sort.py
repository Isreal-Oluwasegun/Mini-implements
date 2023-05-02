from random import randint

def quicksort(array):
    if len(array) < 2:
        return array
    
    pivot = array[randint(0, len(array)-1)]
    low, same, high = [], [], []
    
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)
print(quicksort([23,45,13,678,4,335,567,234,68,23]))