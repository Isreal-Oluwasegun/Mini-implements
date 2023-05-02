def conquer(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
            
        else:
            result.append(right[index_right])
            index_right += 1
            
        if index_left == len(left):
            result += right[index_right:]
            break
        if index_right == len(right):
            result += left[index_left:]
            break
    return result

def divide(array):
    if len(array) < 2:
        return array
    mid_point = len(array)//2
    return conquer(
        left = divide(array[:mid_point]),
        right = divide(array[mid_point:])
    )
        
     

print(divide([23,45,13,678,4,335,567,234,68,23]))
        