def quickSort(arr, start, end):
    if start >= end:
        return 
    pIdx = partitionIdx(arr, start, end)
    quickSort(arr, start, pIdx - 1)
    quickSort(arr, pIdx + 1, end)
    
def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]

def partitionIdx(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left < right:
            swap(arr, left, right)
    swap(arr, start, right)
    return right
            
    
arr = [1, 7, 9, 0, 5, 7]
quickSort(arr, 0, len(arr) - 1)
print(arr)
