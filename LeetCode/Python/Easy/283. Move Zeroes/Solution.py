class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1 = 0
        p2 = 0

        while p2 < len(nums):

            # Find the next non-zero element
            while p2 < len(nums) and nums[p2] == 0:
                p2 += 1

            if p2 < len(nums):

                # Move p1 to a zero position
                while p1 < p2 and nums[p1] != 0:
                    p1 += 1

                # Swap zero with non-zero
                if p1 < p2:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1

            p2 += 1