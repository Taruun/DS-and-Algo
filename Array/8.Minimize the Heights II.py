# So tricky

def getMinDiff(self, arr, n, k):
    arr.sort()
    result = arr[n - 1] - arr[0]
    smallest = arr[0] + k
    largest = arr[n - 1] - k
    for i in range(1, len(arr)):
        if arr[i]-k < 0:
            continue
        minHeight = min(smallest, arr[i] - k)
        maxHeight = max(largest, arr[i - 1] + k)
        result = min(result, maxHeight - minHeight)
    return result