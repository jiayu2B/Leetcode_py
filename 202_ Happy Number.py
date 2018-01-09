class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        arr = []
        while s not in arr:
            arr.append(s)
            s = self.count(s)
            if s == '1':
                return True
        return False
        
    def count(self, strs):
        ans = 0
        for i in strs:
            ans+= (int(i))**2
        return str(ans)
