class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        s1=list(s)
        n=len(s1)
        for i in range(n-2):
            if s1[i]!=s1[i+1] and s1[i]!=s1[i+2] and s1[i+1]!=s1[i+2]:
                c+=1
        return c