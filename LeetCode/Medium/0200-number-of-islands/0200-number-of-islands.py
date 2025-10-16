class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
 
        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
                
            grid[r][c] = '0'

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    num_islands += 1
    
        return num_islands