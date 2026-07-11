class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0] )

        stack = [intervals[0]]

        for i in intervals[1:] :
            start = i[0]
            end  = i[1]
            last = stack.pop()
            if  last[0] <= start <= last[1] :
                stack.append( [ last[0] , max( end,last[1] ) ])
            else:
                stack.append(last)
                stack.append([start,end])
        return stack