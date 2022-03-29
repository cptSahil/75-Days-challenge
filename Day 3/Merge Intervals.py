class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for start,end in intervals:
            prev = ans[-1][1] if ans else -1
            if start > prev:
                ans.append([start,end])
            else:
                ans[-1][1]=max(prev,end)
        return ans