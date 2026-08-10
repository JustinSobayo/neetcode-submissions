class Solution:
    def isValid(self, s: str) -> bool:
        valid = {']':'[', ')':'(', '}':'{'}
        stack = []
        for p in s:
            if p in valid:
                if stack and stack[-1] == valid[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        if not stack:
            return True
        else:
            return False 


