class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        for target in nums1:
            ans = -1
            target_found = False

            for num in nums2:
                if num == target:
                    target_found = True
                elif target_found:
                    if num > target:
                        ans = num
                        break
            
            output.append(ans)
        
        return output
        