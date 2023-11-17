class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        if s[i] == "-":
            sign = 0
            i += 1
        elif s[i] == "+":
            sign = 1
            i += 1
        else:
            sign = 1
        j = i
        while j < len(s) and s[j].isnumeric():
            j += 1
        if i == j:
            x = 0
        else:
            x = int(s[i:j])
        if sign == 0:
            x = -x
        if x <= (-(2**31)):
            x = -(2**31)
        if x >= 2**31:
            x = 2**31 - 1
        return x