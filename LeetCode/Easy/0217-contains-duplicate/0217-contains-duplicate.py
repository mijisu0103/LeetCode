class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        cnt = Counter(nums)

        for num, freq in cnt.items():
            if freq >= 2:
                return True
        return False