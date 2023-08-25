#User function Template for python3

class Solution:
        
    def minSwap (self,arr, n, k) : 
        #Complete the function
        count = 0
        for i in range(n):
            if arr[i] <= k:
                count += 1
        
        bad = 0
        for i in range(count):
            if arr[i] > k:
                bad += 1
            
        ans = bad 
        j = count # to get window size
        for i in range(n):
            # check if j is at position
            if j == n:
                break
            # move window by checking it was bad then bad -= 1 or it is bad then bad += 1
            if arr[i] > k:
                bad -= 1
            if arr[j] > k:
                bad += 1
            ans = min(ans, bad)
            j += 1
        return ans
    

