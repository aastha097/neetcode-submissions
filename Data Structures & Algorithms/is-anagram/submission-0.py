class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t_list=list(t)
        for i in range(len(s)):
            matched=False
            for j in range(len(t_list)):
                if s[i]==t_list[j]:
                    t_list.pop(j)
                    matched=True
                    break
            if not matched:
                return False
        return True

        