class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res, cnt = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
                
        return max(res, cnt)
        