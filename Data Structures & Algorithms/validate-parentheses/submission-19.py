class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {
            '}' : '{', 
            ')' : '(',
            ']' : '[',
        }
        for p in s:
            if p not in valid:
                stack.append(p)
            else:
                if stack and stack[-1] == valid[p]:
                    stack.pop()
                else: return False
                
            print(stack)
        if not stack:
            return True
        else:
            return False
                
                

        