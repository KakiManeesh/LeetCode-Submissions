class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        max_len = float('inf')
        i = 0 
        count = 0
        final = '}'
        for j in range(len(s)):
            if s[j] == '1' :
                count += 1

            while i<=j and  count >k :
                if s[i] == '1' :
                    count -= 1
                i+= 1
            while count == k and i<=j and  s[i] == '0'  : 
                i += 1
            ans = s[i:j+1]
            if count == k   :
                if len(ans) < max_len:
                    max_len = len(ans)
                    final = ans
                elif len(ans) == max_len and final > ans:
                    final = ans
        
        return final if final !='}' else ''