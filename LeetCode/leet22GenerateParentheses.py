class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def generate(s, left, right):
            if left == n and right == n:
                out.append(s)
            elif left == n:
                generate(s + ")", left, right + 1)
            elif left > right:
                generate(s + "(", left + 1, right)
                generate(s + ")", left, right + 1)
            else:
                generate(s + "(", left + 1, right)
        generate("(", 1, 0)
        return out