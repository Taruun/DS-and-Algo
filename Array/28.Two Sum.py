# Unsorted Array 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        # Hashig is use value and index so i for idx and n for value
        # enumerate is used for iterating value and index at same time
        for i, n in enumerate(nums):
            diff = target - n

            if diff in map:
                return [map[diff], i]
                
            map[n] = i


        