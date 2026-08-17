class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        lenght = len(s)
        ans = 0

        for i in range(lenght):
            zero = ones = 0

            for j in range(i,lenght):

                if s[j] == '1':
                    ones+=1
                elif s[j] == '0':
                    zero +=1
                if zero<=k or ones <=k:
                    ans +=1
                else:
                    break
        return ans 
