class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        track = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        track[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                track[r][c] += track[r + 1][c] + track[r][c + 1]
        return track[0][0]


