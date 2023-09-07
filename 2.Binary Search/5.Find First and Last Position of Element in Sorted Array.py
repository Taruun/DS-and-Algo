class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstPosition (nums, target):
            start = 0
            end = len(nums) - 1
            ans = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    ans = mid
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans
        
        def lastPosition(nums, target):
            start = 0
            end = len(nums) - 1
            ans = -1 
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    ans = mid
                    start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return ans

        first = firstPosition (nums, target)
        if first == -1:
            return [-1,-1]
        last = lastPosition (nums, target)
        return [first, last]
   