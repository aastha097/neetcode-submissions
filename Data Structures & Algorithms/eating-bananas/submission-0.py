class Solution:
    def ispossible(self,mid,n,h,piles):
        hr=0
        for i in range(n):
            hr+=math.ceil(piles[i]/mid)
            if hr>h:
                return False
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        n=len(piles)
        while l<=r:
            mid=(l+r)//2
            if self.ispossible(mid,n,h,piles):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans