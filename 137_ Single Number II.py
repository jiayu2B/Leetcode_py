class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = False
            else:
                d[i] = True
        for i in d:
            if d[i] == False:
                return i
