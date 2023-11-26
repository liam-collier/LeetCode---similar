#This solution is heavily inspired by this video:
#https://www.youtube.com/watch?v=HAA8mgxlov8&t=547s
#All credits go to the creator "NeetCode"
#My own (bad) version that passed 354/355 test cases is in the comments below

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
    

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sPointer = 0
        pPointer = 0
        pMemory = False
        amount = 0
        while sPointer < len(s):
            if pPointer >= len(p):
                if pMemory:
                    pPointer = pMemory
                    sPointer = sMemory
                    sMemory += 1
                    if p[pPointer] != ".":
                        while sPointer < len(s) and s[sPointer] != p[pPointer]:
                            sPointer += 1
                    if sPointer == len(s):
                        return False
                else:
                    return False
            if pPointer != len(p) - 1 and p[pPointer + 1] == "*":
                if p[pPointer] == ".":
                    pPointer += 2
                    while pPointer < len(p) - 1 and p[pPointer + 1] == "*":
                        pPointer += 2
                    if pPointer == len(p):
                        return True
                    sMemory = sPointer + 1
                    if  p[pPointer] != ".":
                        while sPointer < len(s) and s[sPointer] != p[pPointer]:
                            sPointer += 1
                    if sPointer == len(s):
                        return False
                    pMemory = pPointer
                    continue
                prev_s = sPointer
                while sPointer < len(s) and s[sPointer] == p[pPointer]:
                    sPointer += 1
                amount = sPointer - prev_s
                pPointer += 2
                cont = True
                while pPointer < len(p) and amount and cont:
                    if p[pPointer] != "." and pPointer != len(p) - 1 and p[pPointer + 1] == "*" and (sPointer == len(s) or s[sPointer] != p[pPointer]):
                        pPointer += 2
                    elif p[pPointer] == s[sPointer - 1]:
                        amount -= 1
                        pPointer += 1
                    else:
                        cont = False
                continue
            if p[pPointer] == ".":
                pPointer += 1
                sPointer += 1
                continue
            if p[pPointer] != s[sPointer]:
                if pMemory:
                    pPointer = pMemory
                    sPointer = sMemory
                    sMemory += 1
                    if p[pPointer] != ".":
                        while sPointer < len(s) and s[sPointer] != p[pPointer]:
                            sPointer += 1
                    if sPointer == len(s):
                        return False
                else:
                    return False
            pPointer += 1
            sPointer += 1
        if pPointer == len(p):
            return True
        while pPointer < len(p):
            print("Status: ", pPointer, p[pPointer])
            if pPointer != len(p) - 1 and p[pPointer + 1] == "*":
                pPointer += 2
            elif p[pPointer] == "." and amount:
                amount -= 1
                pPointer += 1
            else:
                return False
        print("Reached end", pPointer, len(p))
        return pPointer == len(p)
"""