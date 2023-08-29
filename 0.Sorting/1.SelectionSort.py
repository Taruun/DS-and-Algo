def selectionSort(nums):
    for i in range(len(nums)):
        minIdx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minIdx]:
                minIdx = j
        nums[i], nums[minIdx] = nums[minIdx], nums[i]
        

nums = [5,60,60,30,20,10]
selectionSort(nums)
print(nums)
    