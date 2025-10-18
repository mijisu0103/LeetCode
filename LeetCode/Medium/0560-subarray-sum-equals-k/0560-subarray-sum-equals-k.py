from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count, sum_ = 0, 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            sum_ += num
            if (sum_ - k) in prefix_sums:
                count += prefix_sums[sum_ - k]
            prefix_sums[sum_] += 1

        return count