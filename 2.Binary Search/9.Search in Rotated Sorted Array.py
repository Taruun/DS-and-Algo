# If arr[low] <= arr[mid]: This condition ensures that the left part is sorted.
# If arr[low] <= target && target <= arr[mid]: It signifies that the target is in this sorted half. So, we will eliminate the right half (high = mid-1).
# Otherwise, the target does not exist in the sorted half. So, we will eliminate this left half by doing low = mid+1.
# Otherwise, if the right half is sorted:
# If arr[mid] <= target && target <= arr[high]: It signifies that the target is in this sorted right half. So, we will eliminate the left half (low = mid+1).
# Otherwise, the target does not exist in this sorted half. So, we will eliminate this right half by doing high = mid-1.



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

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
        return -1

        