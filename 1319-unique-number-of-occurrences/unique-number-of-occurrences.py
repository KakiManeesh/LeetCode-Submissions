class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = {}

        for i in arr :
            a[i] = a.get(i,0)+1
        
        return len(a.values()) == len(set(a.values()))