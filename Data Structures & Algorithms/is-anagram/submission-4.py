class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1=Counter(s)
        freq2=Counter(t)
        if len(s)!=len(t):
            return False
        for i,count in freq1.items():
            if count!=freq2[i]:
                return False
        return True
