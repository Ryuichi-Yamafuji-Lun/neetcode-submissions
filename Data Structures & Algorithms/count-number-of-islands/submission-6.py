class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        def dfs(x: int, y:int):
            if x not in range(row) or y not in range(col) or grid[x][y] != '1':
                return
            grid[x][y] = '0'

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        total = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    total += 1
                    dfs(r, c)
        return total