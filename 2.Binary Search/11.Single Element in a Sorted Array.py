class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        # base case 
        if len(nums) == 0:
            return nums[0]
        # if nums[0] != nums[1]:
        #     return nums[0]
        # if nums[len(nums) - 1] != nums[len(nums) - 2]:
        #     return [lne(nums) - 1]
        # if nums[mid] != nums[mid -1] and nums[mid] != nums[mid + 1]:
        #         return nums[mid]

        while start < end:
            mid = (start + end) // 2
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                start = mid + 1
            else:
                end = mid
        return nums[start]
        