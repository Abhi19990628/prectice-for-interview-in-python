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

def reversed_list_twopointer(array):
    left=0
    right=len(array)-1
    while (left < right):
        temp=array[left]
        array[left]=array[right]
        array[right] = temp
        left+=1
        right-=1
        
    return array

array=[1,2,3,4,5,6,7]
print(reversed_list_twopointer(array))



def sum_of_array(array):
    plus=0
    for i in array:
        plus += i 
    return plus
array=[1,2,3,4,5,6]
print(sum_of_array(array))

def average_of_array(array , n):
    total=0
    for i in array:
        total += i
    return total/n
array=[1,2,3,4,5,6,7,8,9,10]
n=len(array)
print(average_of_array(array, n))


def swap_of_element(array):
    for i in range(len(array)):
        if array[0 ] < array[n-1]:
            array[0],array[n-1]=array[n-1],array[0]
            
array=[1,2,3,4,5,6,7,8,9,10]
n=len(array)
k=swap_of_element(array)
print(k)   



def swap_by_postion(array , pos1 , pos2):
    array[pos1], array[pos2] = array[pos2] , array[pos1]
    return array

array=[1,2,3,4,5,6,7,8,9,10]
pos1, pos2 = 1 , 6
print(swap_by_postion(array , pos1 , pos2 ))

def find_element_in_array(array, element):
    if element in array:
        return 'exist'
    else:
        return 'not exist'
            
array = [1, 2, 3, 4, 5, 6, 7]
element_to_find = 22
result = find_element_in_array(array, element_to_find)
print(result)

def Total_no_squre (array):
    total_sum=0
    for number in array:
        if number % 2 == 0:
            total_sum += number**2
    return total_sum

array=[1,2,3,4,5,6,7,8,9,10]
k= Total_no_squre(array)
print(k)


def find_missing_number(array):
    n=len(array)+1
    total_sum = n*(n+1)//2
    actual_sum = sum(array)
    return total_sum-actual_sum

array=[1,2,3,4,5,6,8]
missing_number = find_missing_number(array)
print(f"The missing number is:{missing_number}")
