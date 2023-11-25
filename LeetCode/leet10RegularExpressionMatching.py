#This solution is heavily inspired by this video:
#https://www.youtube.com/watch?v=HAA8mgxlov8&t=547s
#All credits go to the creator "NeetCode"

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev = {}
        def search(i, j):
            if (i, j) in prev:
                return prev[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j < len(p) - 1 and p[j + 1] == "*":
                prev[(i, j)] = search(i, j + 2) or (match and search(i + 1, j))
                return prev[(i, j)]
            if match:
                prev[(i, j)] = search(i + 1, j + 1)
                return prev[(i, j)]
            prev[(i, j)] = False
            return False
        
        return search(0, 0)