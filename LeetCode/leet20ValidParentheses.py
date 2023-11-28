class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c not in match:
                stack.append(c)
            elif stack and match[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack