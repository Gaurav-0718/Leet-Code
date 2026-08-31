class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max = len(nums)+1
        for i in range(max-1):
            if nums[i]>=max or nums[i]<=0:
                nums[i] = max
        for i in range(max-1):
            if abs(nums[i]) != max and nums[abs(nums[i])-1]>0:
                nums[abs(nums[i])-1]*=-1
        for i in range(max-1):
            if nums[i]>0:
                return i+1
        return max