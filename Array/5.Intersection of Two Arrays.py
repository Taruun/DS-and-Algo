# Leetcode soln with two pointers 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        ans = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
# this condition checks whether we've already added the   current number to the ans list. If we haven't added it yet (because the list is empty or the last added number is different), then we add it. If the current number is the same as the last added number, we don't add it again to avoid duplicates.
                if not ans or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1
        return ans
    
########################################################################################################
        
# GFG soln with set()
class Solution:    
    def doUnion(self,a,n,b,m):
        i = 0
        j = 0
        ans = set()
        while i < n and j < m:
            if a[i] < b[j]:
                ans.add(a[i])
                i += 1
            elif a[i] > b[j]:
                ans.add(b[j])
                j += 1
            else:
                ans.add(a[i])
                i += 1
                j += 1
        while i < n:
            ans.add(a[i])
            i += 1
        while j < m:
            ans.add(b[j])
            j += 1
        return len(ans)
