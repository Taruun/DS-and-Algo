
def findFloor(arr, target):
    # If <= then go to right:
    # largest element which is <= target
    # last ele which is smaller
    start = 0
    end  = len(arr) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            ans = arr[mid]
            start = mid + 1
        else:
            end = mid - 1
    return ans
 
def findCeil(arr, target):
    # If >= then go to left:
    # smallest element which is >= target
    # first ele which is greater
    start = 0
    end = len(arr) - 1
    ans = - 1
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            ans = arr[mid]
            end = mid - 1
        else:
            start = mid + 1
    return ans
    
    
arr = [3, 4, 4, 7, 8, 10]
target = 5
floor = findFloor(arr, target)
ceil = findCeil(arr, target)
print(floor)
print(ceil)
    