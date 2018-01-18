class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.DFS(s, [])
        return self.res
    #三个函数，一个主函数用于启动。一个DFS， 一个判断是否回文
    def DFS(self, s, s_list):
        if len(s) == 0:
            self.res.append(s_list)
        #当s空了的时候，代表拆完回文了，可以将list插入了
        for i in range(1, len(s)+1):
            if self.isP(s[:i]):
                self.DFS(s[i:], s_list + [s[:i]])
                #对每一个元素，查看是否回文。其中由于用到[:i]所以i需要+1
                
    def isP(self, s):
        if s == s[::-1]:
            return True
