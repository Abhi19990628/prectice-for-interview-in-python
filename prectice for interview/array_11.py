def biggestelement(array):
    small = array[0]
    for i in array:
        if i > small:
            small = i
    return small
array=[1,2,3,4,5,6]
k=biggestelement(array)
print(k)

def find_middel_ele( array , n):
    for i in range(n):
        return  n // 2
array=[1,2,3,4,5,6,7,8,9,10,11,13]
n=len(array)
l=find_middel_ele(array  , n)
print(l)

def find_middel_element(array):
    n=len(array)
    middel= n // 2
    return array[middel]
array=[1,2,3,4,5,6,7]
n=len(array)
k=find_middel_element(array)
print(k)

def minimum_and_maximum(array,n):
    small=array[0]
    big = array[0]
    for i in range(n):
        if array[i]<small:
            small=array[i]
        elif array[i]>big:
            big=array[i]
    return  small , big

array=[1,2,3,4,5,6]
n=len(array)
k=minimum_and_maximum(array,n)
print(k)

array=[1,2,3,4,5,6]
print(array[::-1])


def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
 
    return arr
 
arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))

