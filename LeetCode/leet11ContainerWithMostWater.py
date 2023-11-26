class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        m = 0
        while i != j:
            if height[i] > height[j]:
                m = max(m, height[j] * (j - i))
                j -= 1
            else:
                m = max(m, height[i] * (j - i))
                i += 1
        return m