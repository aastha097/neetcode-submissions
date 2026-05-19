class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_cons=set(nums)
        long=0
        start=None
        for i in long_cons:
            if (i-1) not in long_cons:
                length=1
                while (i+length) in long_cons:
                    length+=1
                #long=max(length,long)
                if length>long:
                    long=length
                    start=i
        if start is not None:
            seq=list(range(start,start+long))
            print(f'{seq}')
        else:
            print('[]')
        return long