

## Brute Force (O(n²))
def twosum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return [i,j]
            


arr = [2,7,11,15]
target = 13

'''
can use dictinary to store each element and its corresponding
index.
and traverse the array for the current element i
first check if target - i is in the dictnary

if it is in dict it means the target value has been found and we
return the indices of (target - i) and i

'''
def twoSSum(arr,target):
    d = {}

    for i,x in enumerate(arr):
        y = target - x

        if y in d:
            return [d[y],i]
        d[x]=i


result = twoSSum(arr,target)
print(result)



''' 
If the given array is sorted 

Use two pointers: one at the start (left), one at the end (right).
If arr[left] + arr[right] > target, move right left.
If arr[left] + arr[right] < target, move left right

Time Complexity: O(n)
Space Complexity: O(1)


'''

def twoSum(arr,target):

    left , right = 0, len(arr)-1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -=1

    return []


print(twoSum(arr,target))

