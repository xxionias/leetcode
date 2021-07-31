"""
542. 01 Matrix - Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat

        cols = len(mat[0])
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    top = dist[i - 1][j] if i > 0 else float("inf")
                    left = dist[i][j - 1] if j > 0 else float("inf")
                    dist[i][j] = 1 + min(top, left)

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    bot = dist[i + 1][j] if i < rows - 1 else float("inf")
                    right = dist[i][j + 1] if j < cols - 1 else float("inf")
                    dist[i][j] = min(dist[i][j], 1 + min(bot, right))

        return dist
