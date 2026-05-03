class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        nums = [i + 1 for i in range(n)]
        left, right = 0, n - 1

        while left <= right:
            mid = int((left + right) / 2)

            left_sum = sum(nums[:mid + 1])
            right_sum = sum(nums[mid:])

            if left_sum == right_sum:
                return mid + 1
            
            elif left_sum > right_sum:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return -1