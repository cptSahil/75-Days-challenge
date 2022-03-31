class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = sum(nums[:3])
        print(ans)
        for i in range(len(nums)):
            start = i+1
            end = n-1
            while start<end:
                s = nums[i]+nums[start]+nums[end]
                if abs(s-target)<abs(ans-target):
                    ans=s
                if s<target:
                    start+=1
                elif s>target:
                    end-=1
                else:
                    return ans
        return ans
    