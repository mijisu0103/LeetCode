class Solution:
    def subsets(self, nums):
        result = []
        
        def dfs(start, visited):
            result.append(visited)
            for idx in range(start, len(nums)):
                dfs(idx + 1, visited + [nums[idx]])
        
        dfs(0, [])
        return result  