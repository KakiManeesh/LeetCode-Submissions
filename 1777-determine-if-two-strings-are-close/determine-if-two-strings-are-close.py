class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a = {}
        b= {}
        
        if len(word1) != len(word2) :
            return False
        
        n = len(word1)

        for i in range(n):
            a[word1[i]] = a.get(word1[i],0) + 1
            b[word2[i]] = b.get(word2[i],0) + 1
        
        return ( sorted(a.values()) == sorted(b.values()) )and  (sorted(a.keys()) == sorted(b.keys()))