from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        freq=defaultdict(int)
        if s=="":
            return 0
        c=0
        maxi=-float('inf')
        for r in range(len(s)):
            if s[r] not in freq:
                c+=1
            freq[s[r]]+=1
            while freq[s[r]]>1:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    freq.pop(s[l])
                c-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi