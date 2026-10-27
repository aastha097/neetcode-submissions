class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1
        maxarea=-float('inf')
        while l<r:
            dist=r-l
            if heights[l]<heights[r]:
                area=heights[l]*dist
                l+=1
            else:
                area=heights[r]*dist
                r-=1
            maxarea=max(maxarea,area)
        return maxarea
        