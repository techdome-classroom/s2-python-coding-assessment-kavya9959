class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I' : 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        c = 0
        i = 0
        n = len(s)

        while i < n - 1:
            if d[s[i]] < d[s[i + 1]]:
                c = c + d[s[i + 1]] - d[s[i]]
                i = i + 2
            else:
                c = c + d[s[i]]
                i = i + 1
        if i < n:
            c = c + d[s[i]]
        
        return c



