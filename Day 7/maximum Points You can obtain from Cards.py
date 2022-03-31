class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = score = sum(cardPoints[:k])
        for i in range(1,k+1):
            score = score - cardPoints[k-i]+cardPoints[-i]
            ans = max(ans,score)
        return ans