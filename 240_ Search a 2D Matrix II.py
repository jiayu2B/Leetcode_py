class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ver = len(matrix) 
        if ver ==0:
            return False
        hor = len(matrix[0])
        if hor == 0:
            return False
        
        #对每一个横数组进行判断，如果最左边和最右边满足于target，则开始搜索。
        for y in range(0,ver):
            if matrix[y][hor-1] >= target and target >= matrix[y][0]:
                if target in matrix[y]:
                    return True
        return False
