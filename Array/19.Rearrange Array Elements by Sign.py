      
# For example, if you have a list 
# my_list = [10, 20, 30, 40, 50] and you use my_list[2:], 
# you would get [30, 40, 50], 
# which are the elements starting 
# from index 2 (inclusive) to the end of the list.
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [num for num in nums if num > 0]
        negative = [num for num in nums if num < 0]
        result = []

        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])

        # Handle remaining elements from the longer array
        remainingElement = min(len(positive), len(negative))
        if len(positive) > len(negative):
            result.extend(positive[remainingElement:])
        else:
            result.extend(negative[remainingElement:])
            
        return result 

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        i = 0
        while i < len(positive):
            result.append(positive[i])
            result.append(negative[i])
            i += 1
        
        return result
        