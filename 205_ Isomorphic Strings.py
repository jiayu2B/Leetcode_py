class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.isTrue(s,t) and self.isTrue(t,s)
    #两次分别检查，防止aa,ab不通过，ab,aa通过
    def isTrue(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
