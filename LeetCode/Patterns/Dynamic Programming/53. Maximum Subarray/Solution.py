class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        curr = 0
        ans = nums[0]

        for i in range(len(nums)):
            curr += nums[i]

            ans = max(ans, curr)

            if curr < 0:
                curr = 0
                left = i + 1

        return ans
