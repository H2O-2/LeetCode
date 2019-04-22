class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        height = len(obstacleGrid)
        length = len(obstacleGrid[0])
        M = [[0] * length for _ in range(height)]

        for i in range(height):
            if obstacleGrid[i][0] == 0:
                M[i][0] = 1
            else:
                break

        for j in range(length):
            if obstacleGrid[0][j] == 0:
                M[0][j] = 1
            else:
                break

        for i in range(1, height):
            for j in range(1, length):
                if obstacleGrid[i][j] == 0:
                    M[i][j] = M[i - 1][j] + M[i][j - 1]

        return M[height - 1][length - 1]


test = Solution()
print(test.uniquePathsWithObstacles([
  [0], [0]
]))
