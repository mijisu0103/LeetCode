class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        first_half, second_half = nums[:n], nums[n:]
        return [element for pair in zip(first_half, second_half) for element in pair]