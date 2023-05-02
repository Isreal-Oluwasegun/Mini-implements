def bubble_sort(array):
    n = len(array) 
    for i in range(n):
        sorted = True
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                sorted = False       
    return array

print(bubble_sort([0, 1, 2, 3, 6, 7, 9, 21]))