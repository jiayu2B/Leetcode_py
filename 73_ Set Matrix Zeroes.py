class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row = [False for i in range(m)]
        colum = [False for i in range(n)]
        #先设计一个row，column的列表，记录哪一个row有0
      
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    colum[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or colum[j]:
                #当出现row为0时，将此行变为0
                    matrix[i][j] = 0
