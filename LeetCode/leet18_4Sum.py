class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr == target:
                        out.append([nums[i], nums[j], nums[left], nums[right]])
                        n = nums[left]
                        while left < len(nums) and nums[left] == n:
                            left += 1
                    elif curr > target:
                        right -= 1
                    else:
                        left += 1
        return out