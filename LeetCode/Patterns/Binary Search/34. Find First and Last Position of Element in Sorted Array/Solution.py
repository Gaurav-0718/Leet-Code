class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_p = bisect_left(nums,target)
        last_p = bisect_right(nums,target)
        return [first_p,last_p-1] if first_p != last_p else [-1,-1]
        