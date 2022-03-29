class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a = 0
        b = 0
        c = Counter()
        for i in nums:
            c[a]+=1
            a+=i
            b+=c[a-k]
        return b