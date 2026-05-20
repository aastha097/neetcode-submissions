class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        width=1
        sum=0
        l,r=0,len(height)-1
        
        tallest=height[l]
        r_tallest=height[r]
        while l<r:
            if tallest<r_tallest:
                l+=1
                tallest=max(tallest,height[l])
                sum+=(width*(tallest-height[l]))
            else:
                r-=1
                r_tallest=max(r_tallest,height[r])
                sum+=width*(r_tallest-height[r])
        return sum


            
        