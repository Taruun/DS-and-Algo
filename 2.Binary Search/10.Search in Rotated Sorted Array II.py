class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True
            
            # Check for duplicates at the start, middle, and end.
            # [3, 3, 3]
            # [start, mid, end]
            while start < mid and nums[start] == nums[mid]:
                start += 1
            while mid < end and nums[mid] == nums[end]:
                end -= 1

            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

        