class Solution:
    def reverseByType(self, s: str) -> str:
        Alpabet = []
        NonAlpabet = []

        for i in s:
            if i.isalpha() :
                Alpabet.append(i)
            else:
                NonAlpabet.append(i)
        
        left = 0 
        right = len(Alpabet) - 1

        while left < right:
            Alpabet[left],Alpabet[right] = Alpabet[right],Alpabet[left]

            left +=1
            right -=1

        left = 0
        right = len(NonAlpabet) - 1

        while left < right:
            NonAlpabet[left],NonAlpabet[right] = NonAlpabet[right],NonAlpabet[left]
             
            left +=1
            right -=1
        
        ans = []
        count_alpha = 0
        count_s = 0
        for i in s:
            if i.isalpha():
                ans.append(Alpabet[count_alpha])
                count_alpha +=1
            else:
                ans.append(NonAlpabet[count_s])
                count_s +=1
        
        return "".join(ans)