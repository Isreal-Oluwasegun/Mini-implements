def insertion_sort(array):
    for i in range(1, len(array)):
        key_element = array[i]
        j = i -1
        while j >=0 and array[j+1] > key_element:
            array[j] = array[j+1]
            j -=1
        array[j+1] = key_element
    return array
        
print(insertion_sort([7,3,5,2]))