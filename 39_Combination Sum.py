class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret
        
        
    def DFS(self, candidates, target, start, _list):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(_list)
        for i in range(start,length):
            if target < candidates[i]:
                return
            #如果target小了，则剪去该枝。如果没小，进行下一步
            self.DFS(candidates, target - candidates[i], i, _list + [candidates[i]])
        
