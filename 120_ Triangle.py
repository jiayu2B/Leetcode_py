class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        arr = [0 for i in range(n)]
        arr[0] = triangle[0][0]
        
        #从第一个list开始，对每一个list从后往前计算。对于某List，最后一个是自己前者和新list位置值到和。对于第一个List， 值为自己和新List的和。
        #对于其他List，则是总控金额前者最小值与List的和。
        for i in range(1,n):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == len(triangle[i]) - 1:
                    arr[j] = arr[j-1] + triangle[i][j]
                elif j == 0:
                    arr[j] = arr[j] + triangle[i][j]
                else:
                    arr[j] = min(arr[j], arr[j-1]) + triangle[i][j]
        return min(arr)
