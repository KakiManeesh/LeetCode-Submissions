class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        count = 0

        for i in range(len(s)):
            p1 = len(expand(i, i))
            p2 = len(expand(i, i+1))
            count += (p1+1)//2 + p2//2
        return count