class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 2:
            return n
        arr = [1,1,2]
        arr += [0 for i in range(n-2)]
        for i in range(3, n+1):
            for j in range(1, i + 1):
              #转换模式
                arr[i] += arr[j-1]*arr[i-j]
        return arr[n]
        
