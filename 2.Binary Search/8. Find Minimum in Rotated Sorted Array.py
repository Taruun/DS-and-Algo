# For min
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start] 
    
# For max
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]: # Chang this line only
                start = mid + 1
            else:
                end = mid
        return nums[start] 
        