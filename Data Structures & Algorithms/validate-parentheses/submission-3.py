import collections as c
class Solution:
    def isValid(self, s: str) -> bool:
        stack = c.deque() #kind of stack but u can use normal list
        closing_para = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for i in range(len(s)):
            if s[i] not in closing_para:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != closing_para[s[i]]:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False