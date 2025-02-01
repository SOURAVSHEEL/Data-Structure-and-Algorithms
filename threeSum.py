## Brute soluton ----> O(n3)

def threesum(arr):
    arr.sort()
    result = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k]==0:
                    result.add((arr[i],arr[j],arr[k]))

    return [list(triplet) for triplet in result]

arr = [-1,0,1,2,-1,-4]
res = threesum(arr)
print(res)



### optimal_solution using sorting and pointer   -----> O(n2)

def threeSum(nums):

    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
                continue
            
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j-1] and j < k:
                    j += 1
        
        return res



            