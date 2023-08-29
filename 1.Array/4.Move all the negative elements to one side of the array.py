def segregateElements(arr, n):
    left = 0
    right = n - 1
    
    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            right -= 1

# Example usage:
arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
segregateElements(arr, n)
print(arr)
