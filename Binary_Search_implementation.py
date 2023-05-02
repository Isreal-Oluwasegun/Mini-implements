def binary_search(elements, value):
    left, right = 0, len(elements) -1
    while left <= right:
        middle = (left + right)//2
        if elements[middle] == value:
            return middle
        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > middle:
            right = middle -1
                
                
                
                
li = [145,25,78,78,997,997,0,12,5667,3423,466,1236,88876,9876,4321,9876,1233,579876,87654]
li_sor = sorted(li)
print(li_sor)
print(binary_search(li_sor, 88876))                                                 