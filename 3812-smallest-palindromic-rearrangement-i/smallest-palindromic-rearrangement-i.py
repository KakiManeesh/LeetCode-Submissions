class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n&1 == 1 :
            middle = s[n//2]
        else:
            middle= ''
        first = s[:n//2]
        first = "".join(sorted(first))
        
        ans = first + middle + first[::-1]

        return ans