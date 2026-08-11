class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zCount = 0
        left = 0
        Max_zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zCount +=1
            
            while zCount > k:
                if nums[left] == 0:
                    zCount-=1
                left+=1

            Max_zeroes = max(Max_zeroes,right-left+1)

        return Max_zeroes