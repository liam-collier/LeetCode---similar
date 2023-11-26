class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        i = 0
        out = []
        while i < len(nums) - 2 and nums[i] <= 0:
            if i == 0 or nums[i] != nums[i - 1]:
                target = nums[i] * (-1)
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    curr = nums[left] + nums[right]
                    if curr == target:
                        out.append([nums[i], nums[left], nums[right]])
                        n = nums[left]
                        while left < len(nums) and nums[left] == n:
                            left += 1
                    elif curr > target:
                        right -= 1
                    else:
                        left += 1
            i += 1
        return out