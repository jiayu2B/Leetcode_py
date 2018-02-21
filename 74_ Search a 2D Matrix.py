class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0: return False
        if len(matrix[0]) == 0: return False
        #边际
        
        for m in range(len(matrix)):
            if matrix[m][0] <= target and matrix[m][len(matrix[m])-1]>= target:
                if target in matrix[m]:
                    return True
                else: return False
        return False
