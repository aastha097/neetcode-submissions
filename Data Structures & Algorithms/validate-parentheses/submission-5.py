class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]#{'[','{','('}
        #{']','}',')'}
        for v in s:
            if v=='(' or v=='{' or v=='[':
                stk.append(v)
            else:
                if not stk:
                    return False
                else:
                    if stk[-1]=='(' and v==')':
                        stk.pop()
                    elif stk[-1]=='{' and v=='}':
                        stk.pop()
                    elif stk[-1]=='[' and v==']':
                        stk.pop()
                    else:
                        return False
        return len(stk)==0