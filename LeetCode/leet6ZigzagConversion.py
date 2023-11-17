class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ls = []
        for i in range(numRows):
            ls.append("")
        cycle = (numRows * 2) - 2 if (numRows * 2) - 2 > 0 else 1
        for i in range(len(s)):
            operation = i % cycle
            if operation < numRows:
                ls[operation] += s[i]
            else:
                ls[numRows - (operation % numRows) - 2] += s[i]
        out = ""
        for string in ls:
            out += string
        return out
