class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mapper = {'a': 0, 'b': 0, 'c': 0}
        i = 0
        total = 0
        n = len(s)
        for j in range(len(s)):
            mapper[s[j]] += 1
            
            while mapper['a'] > 0 and mapper['b'] > 0 and mapper['c'] > 0:
                total += n-j
                mapper[s[i]] -= 1
                i += 1
        
        return total