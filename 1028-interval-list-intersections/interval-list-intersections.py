class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]: 

        i = j = 0
        m = len(firstList )
        n = len(secondList)      

        result = []

        while i< m and j < n :
            first = firstList[i]
            second  = secondList[j]
            if max(first[0], second[0]) <= min(first[1], second[1]):
                result.append([max(first[0], second[0]), min(first[1], second[1])])
            
            if first[1] < second[1] :
                i +=1
            else:
                j +=1
        return result