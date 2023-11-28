class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = [""]
        match = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
            }
        for n in digits:
            new = []
            for s in out:
                for c in match[int(n)]:
                    new.append(s + c)
            out = new
        if len(out) == 1:
            return []
        return out