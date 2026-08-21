class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        max_ =0
        n = len(s)
        i= 0 
        for j in range(n):
            while s[j] in window :
                window.remove(s[i])
                i+=1
            window.add(s[j])
            max_ = max( max_ , j-i+1 )

        return max_