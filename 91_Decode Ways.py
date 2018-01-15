class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        res = [1,1]
        #三种情况，一种是出现11~26除了20这样可以分解成两个的数字。那么可能的方法为前一位可能方法和前第二位可能的方法之和。第二种情况是出现了10,20的时候，那么这时的解法只有10，则解法将为前第二位的解法数量。
        #第三种是其他。只要没有奇怪的0，都是前一位的解法，比如‘27’。如果还识别不出来，那就是出问题了，比如‘100’，返回0
        for i in range(2,len(s) + 1):
            if 11<=int(s[i-2:i])<=26 and s[i-1] != '0':
                res.append(res[i-2]+res[i-1])
            elif int(s[i-2:i])==20 or int(s[i-2:i])==10:
                res.append(res[i-2])
            elif s[i-1] != '0':
                res.append(res[i-1])
            else:
                return 0
        return res[-1]
