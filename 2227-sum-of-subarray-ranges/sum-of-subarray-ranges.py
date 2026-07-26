class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        stack =[]
        n = len(nums)

        #LEFT 
        left_min = [0]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i] :
                stack.pop()
            
            left_min[i] = i+1 if not stack else i - stack[-1]
            stack.append(i)

        left_max = [0]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i] :
                stack.pop()
            
            left_max[i] = i+1 if not stack else i - stack[-1] 
            stack.append(i)
        
        # RIGHT
        right_min = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] > nums[i] :
                stack.pop()
            
            right_min[i] = n- i if not stack else stack[-1] - i 
            stack.append(i)

        right_max = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i] :
                stack.pop()
            
            right_max[i] = n-i if not stack else  stack[-1] - i 
            stack.append(i)

        total = 0
        for i in range(n):
            max_ = nums[i] * left_max[i] * right_max[i]
            min_ = nums[i] * left_min[i] * right_min[i]
            total += max_-min_
        return total