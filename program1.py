class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif stack and stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack and stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack and stack[-1] == '{' and i == '}':
                stack.pop()
            else: 
                return False
        return (len(stack)==0)

    



  

