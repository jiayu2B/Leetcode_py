class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)== 0:
            return []
        self.res = []
        nums.sort()
        self.DFS(nums, [], 0)
        #标准dfs
        return self.res
    
    def DFS(self, nums, _list, start):
        if _list not in self.res:
            self.res.append(_list)
        for i in range(start, len(nums)):
            self.DFS(nums, _list+[nums[i]], i+1)
