def subArrayExists(self,arr,n):
        
    currentSum = 0
    setForSum = set()
        
    for i in arr:
        currentSum += i
            
        if currentSum == 0 or currentSum in setForSum:
                return True
        else:
            setForSum.add(currentSum)
                
    return False
