class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        subCont = 0
        Csum = 0

        for i in nums:
            Csum += i

            req = Csum - k

            if req in seen:
                subCont += seen[req]

            seen[Csum] = seen.get(Csum, 0) + 1

        return subCont