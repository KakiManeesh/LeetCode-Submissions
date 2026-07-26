class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # left[i] = count of elements to the left >= arr[i]
        left = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i if not stack else i - stack[-1] - 1
            stack.append(i)
        

        right = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = n - 1 - i if not stack else stack[-1] - i - 1
            stack.append(i)


        total = 0
        for i in range(n):
            total += arr[i] * (left[i] + 1) * (right[i] + 1)
            total %= MOD
        
        return total