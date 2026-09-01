class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero=0
        for i in nums:
            if i!=0:
                prod*=i
            else:
                zero+=1
        ans=[]
        for i in nums:
            if i==0:
                if zero>1:
                    ans.append(0)
                else:
                    ans.append(prod)
            else:
                if zero>0:
                    ans.append(0)
                else:
                    ans.append(prod//i)
                    


        return ans