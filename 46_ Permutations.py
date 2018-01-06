class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self.DFS(nums,sub)
        return self.res
    #DFS的一种应用
    def DFS(self, candidates,_list):
        if len(_list) == len(candidates):
            self.res.append(_list[:])
            return
        for i in candidates:
            if i in _list:
                continue
            _list.append(i)
            self.DFS(candidates, _list)
            _list.remove(i)
   
