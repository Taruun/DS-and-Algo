class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >  target:
                # [1,2,3,4,5,6,7,8,9]
                # i      k         j
                # i    j k
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
        # Recursion
        # def binarySearch(nums, start, end, target):
        #     if start > end:
        #         return - 1
        #     mid = (start + end) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         return binarySearch(nums, start, mid - 1, target)
        #     else:
        #         return binarySearch(nums, mid + 1, end, target)
        # return binarySearch(nums, 0, len(nums) -1, target)

