class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        ans = nums[0]
        curr = 0

        for i in range(n):
            curr += nums[i]

            if curr < 0:
                ans = max(ans, curr)

            while left <= i and curr < 0:
                curr -= nums[left]
                left += 1

            ans = max(ans, curr)

        return ans
