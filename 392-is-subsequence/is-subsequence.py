from re import *
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        if not s :
            return True
        pattern = s[0]
        s=s[1:]
        for i in s :
            pattern = pattern + ".*?" + i
        matchs = findall(pattern,t)
        
        if matchs :
            return True
        else:
            return False
            '''

        i = 0
        n = len(s)
        for j in t :
            if i == n :
                return True
            
            if s[i] == j :
                i+=1
        return i==n