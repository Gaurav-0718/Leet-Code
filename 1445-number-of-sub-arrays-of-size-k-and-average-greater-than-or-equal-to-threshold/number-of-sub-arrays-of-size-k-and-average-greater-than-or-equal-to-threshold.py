class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        target = k*threshold
        window = sum(arr[:k])
        count = 0
        if window >= target:
            count +=1

        for i in range(k,len(arr)):
            window -= arr[i-k]
            window += arr[i]

            if window >= target:
                count+=1
        return count