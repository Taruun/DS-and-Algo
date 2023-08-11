def getMinMax( a, n):
    minElement = a[0]
    maxElement = a[0]
    for idx in range(n):
        if a[idx] < minElement:
            minElement = a[idx]
        elif a[idx] > maxElement:
            maxElement = a[idx]
       
    return minElement, maxElement
    
    