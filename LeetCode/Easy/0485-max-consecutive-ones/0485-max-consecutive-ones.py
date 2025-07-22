class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res, cnt = 0, 0
        
        for i in nums:
            if i == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        return max(res, cnt)
            