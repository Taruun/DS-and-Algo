class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSumSoFar = 0
        maxEndingHere = nums[0]
        
        for idx in nums:
            maxSumSoFar = maxSumSoFar + idx
            maxEndingHere = max(maxEndingHere, maxSumSoFar)

            if maxSumSoFar < 0:
                maxSumSoFar = 0

        return maxEndingHere


        