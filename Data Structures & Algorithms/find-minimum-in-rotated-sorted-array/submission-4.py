class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        peak=-1
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                peak=i-1
        l=0
        r=n-1
        #while l<r:
        #    mid=(l+r)//2
        #    if nums[mid]>nums[r]:
        #        l=mid+1
        #    else:
        #        r=mid
        if peak!=-1:
            return nums[peak+1]
        else:
            return nums[0]