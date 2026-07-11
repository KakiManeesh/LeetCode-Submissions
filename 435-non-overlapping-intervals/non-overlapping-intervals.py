class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1] )
        total = 0
        till_now = float('-inf')

        for i in intervals :
            if i[0] < till_now :
                total +=1
            else:
                till_now = i[1]
        return total