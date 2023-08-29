# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def bubbleSort(nums):
    for i in range(len(nums)):
        didSwapped = 0
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                didSwapped = 1
        if didSwapped == 0:
            break
        

nums = [5,60,60,30,20,10]
bubbleSort(nums)
print(nums)
    