class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                v = target - nums[i]
                idx = nums.index(v)
                if idx != i:  
                    seen.append(i)
                    seen.append(idx)
                    return seen
        return seen
