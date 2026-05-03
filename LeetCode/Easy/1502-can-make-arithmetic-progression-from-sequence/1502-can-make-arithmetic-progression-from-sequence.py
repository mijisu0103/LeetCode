class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        arr.sort()
        d = arr[1] - arr[0]
      
        # Check if all consecutive pairs have the same difference
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != d:
                return False
      
        return True