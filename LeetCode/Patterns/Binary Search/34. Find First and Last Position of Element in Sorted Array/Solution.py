class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find first occurrence
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        first = low

        # Find last occurrence
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1

        last = low

        if first == last:
            return [-1, -1]

        return [first,last-1]