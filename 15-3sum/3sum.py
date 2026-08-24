class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        set_ = set()
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums) -1
            
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total  == 0:
                    t = (nums[i],nums[left],nums[right])
                    set_.add(t)
                    left +=1
                    right -=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
        return list(set_)