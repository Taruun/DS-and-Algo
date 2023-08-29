class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1, ele2  = float("-inf"), float("-inf")
        count1, count2 = 0, 0

        for i in nums:
            if count1 == 0 and ele2 != i:
                ele1 = i
                count1 = 1
            elif count2 == 0 and ele1 != i:
                ele2 = i
                count2 = 1
            elif ele1 == i:
                count1 += 1 
            elif ele2 == i:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for i in nums:
            if i == ele1:
                count1 +=1
            elif i == ele2:
                count2 += 1
        
        result = []
        if count1 > len(nums) // 3:
            result.append(ele1)
        if count2 > len(nums) // 3:
            result.append(ele2)

        
        return result
        