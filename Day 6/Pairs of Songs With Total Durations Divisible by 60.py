class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        pair = {}
        for i in time:
            a = i%60
            if (60-a) in pair:
                count = count+pair[(60-a)]
            if a==0 and a in pair:
                count = count+pair[a]
            if a in pair:
                pair[a]+=1
            else:
                pair[a] = 1
        return count