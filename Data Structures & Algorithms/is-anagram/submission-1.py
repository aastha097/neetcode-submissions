class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen=[]
        for c in s:
            seen.append(c)
        for c in t:
            if c in seen:
                seen.remove(c)
            else:
                return False
        return True

