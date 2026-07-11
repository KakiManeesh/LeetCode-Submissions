class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        arr = sorted(nums)
        n = len(nums)
        
        mid = (n + 1) // 2
        s, l = mid - 1, n - 1
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[s]
                s -= 1
            else:
                nums[i] = arr[l]
                l -= 1