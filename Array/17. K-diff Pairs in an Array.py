class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 1
        ans = set()
        
        while j < len(nums):
            diff = nums[j] - nums[i]
            if diff == k:
                ans.add((nums[i], nums[j]))
                i += 1
                j += 1
            elif diff > k:
                i += 1
            else:
                j += 1
            if i == j:
                j += 1
                
        return len(ans)
