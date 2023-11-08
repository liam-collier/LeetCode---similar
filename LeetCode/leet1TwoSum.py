class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} #Store values found
        out = [] #Store the output
        for i in range(len(nums)):
            check = target - nums[i]
            if check in hash:
                out.append(i)
                out.append(hash[check])
                break
            hash[nums[i]] = i
        return out