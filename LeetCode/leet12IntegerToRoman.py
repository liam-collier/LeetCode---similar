class Solution:
    def intToRoman(self, num: int) -> str:
        translate = {
            1: ["I", "X", "C", "M"],
            4: ["IV", "XL", "CD"],
            5: ["V", "L", "D"],
            9: ["IX", "XC", "CM"]
        }
        i = 3
        roman = ""
        while i >= 0:
            if 10 ** i <= num:
                d = (num // (10 ** i)) % 10
                if d in translate:
                    roman += translate[d][i]
                elif d < 4:
                    roman += translate[1][i] * d
                else:
                    roman += translate[5][i] + translate[1][i] * (d - 5)
            i -= 1
        return roman