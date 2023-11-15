class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        found = {}
        if s:
            found[s[0]] = 0
        substr = [0]
        if len(s) == 1:
            substr.append(1)
        while right < len(s):
            if found.get(s[right]) is None:
                found[s[right]] = right
            elif found[s[right]] >= left:
                substr.append(right - left)
                left = found[s[right]] + 1
                found[s[right]] = right
            else:
                found[s[right]] = right
            if right == len(s) - 1:
                substr.append(right - left + 1)
            right += 1
        return max(substr)