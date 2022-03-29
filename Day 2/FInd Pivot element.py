class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        for i,j in enumerate(nums):
            if r-j == l:
                return i
            else:
                r -= j
                l += j
        return -1