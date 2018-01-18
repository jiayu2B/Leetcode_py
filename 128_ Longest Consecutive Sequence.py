class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {x : False for x in nums}
        maxlen = 0
        #建立一个dict，所有元素标为False。当用到后改成True。
        #对一个元素进行左右查值，将每一块都查出来。
        
        for i in d:
            if d[i] == False:
                curr = i + 1
                lenright = 0
                while curr in d:
                    lenright += 1
                    d[curr] = True
                    curr += 1
                    
                curr = i - 1
                lenleft = 0
                while curr in d:
                    lenleft += 1
                    d[curr] = True
                    curr -= 1
                maxlen = max(maxlen, lenright + lenleft + 1)
        return maxlen
