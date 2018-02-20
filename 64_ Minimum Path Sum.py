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
        #初始化第一列第一行。
            
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = min( arr[i-1][j] + grid[i][j], arr[i][j-1] + grid[i][j])
                #动态规划，每一个格子最小的值为上左各自最小值加本值
        return arr[-1][-1]
