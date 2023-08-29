# Using Dictionary
def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        ans = [ ]
        i = 0
        j = 0
        k = 0
        
        while i<n1 and j<n2 and k<n3:
            if A[i] == B[j] == C[k]:
                if not ans or ans[-1] != A[i]:
                    ans.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
                
        return ans

# Using Set
def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        ans = []
        setForDuplicates = set()
        i, j, k = 0, 0, 0
        
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] == C[k]:
                setForDuplicates.add(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        ans = sorted(setForDuplicates) 
        return ans
