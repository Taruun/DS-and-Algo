def merge(arr, start, mid, end):
    m = arr[start:mid + 1]
    n = arr[mid + 1: end + 1]
    left, right = 0,0
    result = start
    
    while left < len(m) and right < len(n):
        if m[left] <= n[right]:
            arr[result] = m[left]
            left += 1
        else:
            arr[result] = n[right]
            right += 1
        result += 1
        
    while left < len(m):
        arr[result] = m[left]
        left += 1
        result += 1
        
    while left < len(n):
        arr[result] = n[right]
        right += 1
        result += 1
    
def mergeSort(arr, start, end):
    if start >= end: 
        return
    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid, end)
    
    
arr = [1, 4, 6, 7, 843, 3, 2, 1]
mergeSort(arr, 0, len(arr) - 1)
print(arr)  # Print the sorted array
