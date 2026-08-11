class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        lst = list(s)
        left = 0
        right = k-1

        while left < right:
            lst[left],lst[right] = lst[right],lst[left]
            left +=1
            right  -=1
        
        return "".join(lst)