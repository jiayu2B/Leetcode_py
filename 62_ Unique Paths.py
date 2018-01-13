class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            _list = [[1]]
        elif m == 1 and n > 1:
            _list = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            _list = [[1] for i in range(m)]
        
        else:
            _list = [[0 for i in range(n)] for i in range(m)]
            
            #建立一个list，这个状态转移函数是_list[i][j] = _list[i-1][j] + _list[i][j-1]
            #1 1 1 1
            #1 2 3 4
            #1 3 6 7
            #1 4 10 17
            for i in range(n):
                _list[0][i] = 1
            for i in range(m):
                _list[i][0] = 1
            for i in range(1,m):
                for j in range(1,n):
                    _list[i][j] = _list[i-1][j] + _list[i][j-1]
        return _list[m-1][n-1]
                
