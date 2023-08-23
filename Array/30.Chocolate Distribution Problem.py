class Solution:
    def findMinDiff(self, A,N,M):
        # fixed Window problem
        # code here
        i = 0
        j = M - 1
        diff = float("inf")
        A.sort()
        
        while j < N:
            diff = min(diff, A[j] - A[i])
            j += 1
            i += 1
        
        return diff
            