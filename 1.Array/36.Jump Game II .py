class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            maxJumps = 0
            for i in range(l, r + 1):

            # get max of maxJumps or 
            # idx + value and update with maxJumps
                maxJumps = max(maxJumps, i + nums[i])

            l = r + 1 # update window size 
            r = maxJumps # update window size 
            res += 1

        return res

