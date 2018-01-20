class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = [-1 for i in range(256)]
        #设置一个256位的dict，初始值-1。移动i时将相应字母的值设为i，如果l比i小，则dict到i位置在计算。
        res = 0
        l = 0
        for i in range(len(s)):
            if d[ord(s[i])] != -1:
                while l <= d[ord(s[i])]:
                    d[ord(s[l])] = -1
                    l += 1
            res = max(res, i - l + 1)
            d[ord(s[i])] = i
        return res
 
