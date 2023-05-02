# Bubble sort implementation with python
def bubble_sort(array):
    array_length = len(array) 
    
    # Loop through the array
    for i in range(array_length):
        sorted = True
        for j in range(array_length-1):
            if array[j] > array[j+1]: 
                array[j], array[j+1] = array[j+1], array[j] # swap items if not in oreder
                sorted = False       
    return array

