class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.sti(num1)*self.sti(num2))
        
    def sti(self,nums):
        res = 0
        pro = 1
        nums = nums[::-1]
        #需要倒序一次，用来string into int
        for i in nums:
            t = ord(i)-48
            res+=pro*t
            pro=pro*10
        return res
