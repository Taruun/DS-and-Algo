class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)- 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        # return -1

        # ans = -1
        # for i in range(len(nums)):
        #     idx = abs(nums[i]) - 1  # Corrected the index
        #     if nums[idx] < 0:
        #         return abs(nums[i])  # Return the repeating element
        #     nums[idx] *= -1
        # return ans

        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]] 
        return nums[0]
