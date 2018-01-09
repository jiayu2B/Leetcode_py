class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        i = 0
        #当m与n不等时，拆后缀。直到前缀相等
        while m != n:
            m = m>>1
            n = n>>1
            i += 1
        return m<<i
