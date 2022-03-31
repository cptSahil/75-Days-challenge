class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        p = [[] for i in range(target+1)]
        for  c in candidates:
            for i in range(target+1):
                if i<c:
                    continue
                if i==c:
                    p[i].append([c])
                else:
                    for l in p[i-c]:
                        p[i].append(l+[c])
        return p[target]