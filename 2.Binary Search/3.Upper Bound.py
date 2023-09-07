# If lowerBound >= then go to left:
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end ) // 2
        # Just = sigh changed
        if arr[mid] > target:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
    
arr = [1,2,4,5,6,7,8,9]
target = 6
res = binary_search(arr, target)
print(res)