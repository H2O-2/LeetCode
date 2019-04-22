class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        length = len(grid[0])
        M = [[grid[0][0]] * length for _ in range(height)]

        for i in range(1, height):
            M[i][0] = grid[i][0] + M[i - 1][0]

        for j in range(1, length):
            M[0][j] = grid[0][j] + M[0][j - 1]

        for i in range(1, height):
            for j in range(1, length):
                M[i][j] = min(M[i-1][j], M[i][j-1]) + grid[i][j]

        return M[-1][-1]


test = Solution()
print(test.minPathSum([[1,2],[5,6],[1,1]]))
