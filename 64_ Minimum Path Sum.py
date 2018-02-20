class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        arr = [[0 for i in range(n)] for i in range(m)]
        arr[0][0] = grid[0][0]
        for i in range(1,m):
            arr[i][0] = arr[i-1][0] + grid[i][0]
        for j in range(1,n):
            arr[0][j] = arr[0][j-1] +grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = min( arr[i-1][j] + grid[i][j], arr[i][j-1] + grid[i][j])
                
        return arr[-1][-1]
