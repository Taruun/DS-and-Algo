class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)  - 1

        for i in range(len(nums) - 1, -1, -1):
            # check if current idx + value is >= to the goal
            # i.e. its next element (goal)
            if i + nums[i] >= goal:
                goal = i

        return goal == 0 