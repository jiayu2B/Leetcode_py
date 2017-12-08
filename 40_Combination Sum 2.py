class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        candidates.sort()
        self.DFS(candidates, target,0, [])
        return Solution.res
        
    def DFS(self, candidates, target, start,  _list):
        length = len(candidates)
        if target == 0 and _list not in Solution.res:
            Solution.res.append(_list)
            return 
        for i in range(start,length):
            if candidates[i] > target:
                return
            self.DFS(candidates, target - candidates[i], i+1, _list + [candidates[i]])
    #做法类似39.
