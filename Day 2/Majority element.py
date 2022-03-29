class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        Current = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i]!= Current:
                count-=1
                if count==0:
                    Current = nums[i]
                    count = 1
            else:
                count += 1
        return Current