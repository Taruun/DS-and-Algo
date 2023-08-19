class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        s = set(nums)
        longest = 1
        for num in nums:
            if num - 1 not in s:
                # Initialize count to 1, 
                # as we've found at least one consecutive number
                count = 1
                # Start counting from the next number
                current = num + 1

                while current in s:
                    count += 1
                    current += 1
                    
                longest = max(longest, count)
            
        return longest

        
        