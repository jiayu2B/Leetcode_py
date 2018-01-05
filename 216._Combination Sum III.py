class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        sub = [1,2,3,4,5,6,7,8,9]
        Solution.res = []
        Solution.ref = k
        self.DFS(sub, n, 0, 0, [])
        return Solution.res
    #深度优先搜索
    def DFS(self, sub, target, k, start, _list):
        length = len(sub)
        if target == 0 and _list not in Solution.res and k == Solution.ref:
            Solution.res.append(_list)
            return
        for i in range(start, length):
            if sub[i] > target:
                return
            if k >=Solution.ref:
                return
            #两个限制条件，一个数组内部数的数量，一个是大小。
            self.DFS(sub, target - sub[i], k+1, i+1, _list+[sub[i]])
