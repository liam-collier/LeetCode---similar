class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if abs(curr - target) < abs(closest - target):
                    closest = curr
                    if closest == target:
                        return target
                if curr > target:
                    right -= 1
                else:
                    left += 1
        return closest