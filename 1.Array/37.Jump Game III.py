class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0] * len(arr)
        # visited = [0 for num in arr]

        def helper(arr, i):
            if i >= len(arr) or i < 0:
                return False

            if arr[i] == 0:
                return True

            # if i already been discover in recursive tree then false
            # to avoid repetations and go to that value again
            if visited[i]:
                return False
            
            visited[i] = 1

            j = helper(arr, i + arr[i])
            k = helper(arr, i - arr[i])

            return j or k
        
        return helper(arr, start)