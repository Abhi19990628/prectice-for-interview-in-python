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


def find_missing_number(array):
    n=len(array)+1
    total_sum = n*(n+1)//2
    actual_sum = sum(array)
    return total_sum-actual_sum

array=[1,2,3,4,5,6,8]
missing_number = find_missing_number(array)
print(f"The missing number is:{missing_number}")

# Maximum Subarray Problem (Kadane's Algorithm)
# Problem: Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
def max_subarray(nums):
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))  # Output: 6



# Longest Increasing Subsequence (LIS)
# Problem: Given an unsorted array of integers, find the length of the longest increasing subsequence.
def length_of_lis(nums):
    if not nums:
        return 0

    lis = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)

# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4


# Array Product Excluding Self
# Problem: Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
def product_except_self(nums):
    length = len(nums)
    answer = [1] * length

    left = 1
    for i in range(length):
        answer[i] = left
        left *= nums[i]

    right = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer

# Example
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]


#. Merge Intervals
# Problem: Given a collection of intervals, merge all overlapping intervals.

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]


# Trapping Rain Water
# Problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water

# Example
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6


