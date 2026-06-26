class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0 

        current = 0

        loki = 0
        thor = len(height)-1

        while loki < thor :

            current = min(height[loki] , height[thor]) * (thor - loki)
            max_area = max(max_area , current)

            if height[loki] < height[thor]:
                loki += 1
            else:
                thor -= 1 
        return max_area