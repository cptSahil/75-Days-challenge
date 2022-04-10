class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        x = Counter()
        x[0]=1
        for i in nums:
            sums+=i
            diff = sums%k
            count+=x[diff]
            x[sums%k]+=1
        return count