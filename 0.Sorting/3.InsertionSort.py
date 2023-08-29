# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def bubbleSort(nums):
    for i in range(1, len(nums)):
        current = i - 1
        while current >= 0 and nums[current + 1] < nums[current]:
            nums[current], nums[current + 1] = nums[current + 1], nums[current]
            current -= 1

nums = [5,60,60,30,20,10]
bubbleSort(nums)
print(nums)
    