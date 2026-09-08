class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        hash = {}
        n = len(groupSizes)
        for i in range(n):
            if groupSizes[i] not in hash :
                hash[groupSizes[i]] = []
            hash[groupSizes[i]].append(i)
        
        ans = []

        for key,value in hash.items() :
            if key == len(value) :
                ans.append(value)
                continue
            
            for i in range(0,len(value),key):
                row = [  ]
                for j in range(i,i+key):
                    row.append(value[j])
                ans.append(row)
        return ans