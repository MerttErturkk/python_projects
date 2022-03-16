class Solution(object):
    def isValid(self, s):
        pairs = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in pairs: 
                stack.append(i)
            elif len(stack) == 0 or pairs[stack.pop()] != i:
                return False
        return len(stack) == 0