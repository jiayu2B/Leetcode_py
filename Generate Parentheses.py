class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.Iter("",n,n)
        return self.res
    
    def Iter(self,the_str,l,r):
        if l == 0 and r == 0:
            self.res.append(the_str)
        if l > 0:
            self.Iter(the_str+'(',l-1,r)
        if r > 0 and r > l:
            self.Iter(the_str+')',l,r-1)
            
""" 
使用迭代，我们需要的是一堆可用括号，要保证在任何位置左括号的大于等于右括号。n=3代表有3对左右括号，l>0时候加入左括号，r>l（右括号剩余较多代表左括号多）时加入右括号。当l,r全等于0的时候，将字符串加进去。
"""
        
