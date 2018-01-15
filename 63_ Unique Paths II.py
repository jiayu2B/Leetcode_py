class Solution(object):
    def uniquePathsWithObstacles(self, og):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(og) == 0 or len(og[0]) == 0:
            return 0
           
        #制作列表
        m, n =len(og), len(og[0])
        s = [[-1 for i in range(n)] for i in range(m)]
        
        #设置第一个为1,
        s[0][0] = 1
        #把障碍列出来，凡是障碍都是不能达到的0
        for i in range(m):
            for j in range(n):
                if og[i][j] == 1:
                    s[i][j] = 0
                    
        #初始化最上面和最左边一排
        for i in range(m-1):
            if s[i+1][0] == -1: 
                s[i+1][0] = s[i][0]
        for i in range(n-1):
            if s[0][i+1] == -1: 
                s[0][i+1] = s[0][i]
        #填满整个数组
        for i in range(1,m):
            for j in range(1,n):
                if s[i][j] == -1:
                    s[i][j] = s[i-1][j] + s[i][j-1]
        return s[-1][-1]
