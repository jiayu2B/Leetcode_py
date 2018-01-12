import re
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        while len(path) > 1 and path[-1] == '/':
            path = path[:-1]
        stack_o = path.split('/')
        stack = []
        for i in stack_o:
            #正则表达式检测到英文，压栈
            if re.search('\w', i):
                stack.append(i)
            #有种特殊的‘...’存在，需要考虑
            elif re.match('\\.\.\.+',i):
                stack.append(i)
            #检测到‘..’，出栈
            elif i == '..' and stack != []:
                stack.pop()
        print(stack_o)
        res = '/'
        res+= '/'.join(stack)
        
        return res
