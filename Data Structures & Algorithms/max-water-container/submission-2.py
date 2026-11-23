class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1 
        
        area = []

        while l <= r:
            
            contains = min(heights[l] , heights[r] ) * (r - l)
            area.append(contains)
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max(area)
        

        


        