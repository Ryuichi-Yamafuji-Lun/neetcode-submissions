class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROW, COL = len(grid), len(grid[0])
        def dfs(r, c):
            if r not in range(ROW) or c not in range(COL): return
            if grid[r][c] != "1": return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count