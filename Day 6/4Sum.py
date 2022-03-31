class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        l = []
        def nsum(n,start,target):
            if n!=2:
                for i in range(start, len(nums)-n+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    l.append(nums[i])
                    nsum(n-1,i+1,target-nums[i])
                    l.pop()
                return
            a = start
            b = len(nums)-1
            while a<b:
                s = nums[a]+nums[b]
                if s<target:
                    a+=1
                elif s>target:
                    b-=1
                else:
                    res.append(l+[nums[a],nums[b]])
                    a+=1
                    while a<b and nums[a]==nums[a-1]:
                        a+=1
    
        nsum(4,0,target)
        return res