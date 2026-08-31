class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = {}
        ans=0
        flag=False
        for i in s:
            i=i.lower()
            a[i]=a.get(i,0)+1
        for i in a:
            ans+=(a[i]//2)*2
            if not flag:
                if a[i]%2==1:
                    ans+=1
                    flag=True

        return ans