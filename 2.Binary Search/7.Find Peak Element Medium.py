class Solution:
    # When there is end = mid / start = mid put while start < end
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
                
        return start
        
# If you want to add start <= end then check below
# So for the empty array or sorted array
class Solution:
    # When there is end = mid / start = mid put while start < end
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            # This check
            if start == end:
                return start
            
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
                
        return start