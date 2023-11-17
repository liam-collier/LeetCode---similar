class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        negative = True if s[0] == "-" else False
        length = len(s) if not negative else len(s) - 1
        sreverse = s[::-1] if not negative else "-" + s[::-1][:-1]
        xreverse = int(sreverse)
        if xreverse < -2147483647 or xreverse > 2147483647:
            return 0
        return xreverse