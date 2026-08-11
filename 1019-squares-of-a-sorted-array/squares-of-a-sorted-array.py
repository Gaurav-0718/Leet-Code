class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        v = [x*x for x in nums]
        v.sort()
        
        return v