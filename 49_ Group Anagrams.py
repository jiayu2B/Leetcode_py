class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        #d用来做索引，每出现一个字，先sort看看d里面有没有。有的话加上，没有的话添加。
        res = []
        for i in strs:
            tem = ''.join(sorted(i))
            #普通的sorted函数只会让i变成一个单字符串列表。需要join才能用。
            if tem in d:
                d[tem] += [i]
            else:
                d[tem] = [i]
        
        for i in d:
            tem = d[i]
            res.append(tem)
        return res
                
