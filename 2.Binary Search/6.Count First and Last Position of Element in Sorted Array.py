def firsOcurrence(nums, target):
    start = 0
    end = len(nums) - 1
    ans = -1
    while start <= end:
        mid = (start + end) //2
        if nums[mid] == target:
            ans = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return ans

def lastOcurrence(nums, target):
    start = 0
    end = len(nums) - 1
    ans = -1
    while start <= end:
        mid = (start + end) //2
        if nums[mid] == target:
            ans = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return ans
    
def firstAndLastOcurrence(nums, target):
    first =  firsOcurrence(nums, target)
    if first == -1:
        return [-1,-1]
    last = lastOcurrence(nums, target)
    return [first, last]
    
def count(nums, target):
    first, last = firstAndLastOcurrence(nums, target)
    if first == -1:
        return 0
    return last - first + 1


nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
target = 3
result = count(nums, target)
print(result)