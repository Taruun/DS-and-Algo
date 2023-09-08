class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            square = mid * mid
            if square == x:
                return mid
            if square > x:
                end = mid - 1
            else:
                 ans = mid
                 start = mid + 1
        return ans 
        