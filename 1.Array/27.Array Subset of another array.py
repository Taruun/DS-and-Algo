def isSubset( a1, a2, n, m):
    counts = {}
    
    for i in a1:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
            
    for i in a2:
        if i not in counts or counts[i] <= 0:
            return "No"
        counts[i] -= 1
    
    return "Yes"