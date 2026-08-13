class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = ["a","e","i","o","u"]
        word = list(s)

        window = word[:k]
        count = 0

        for i in window:
            if i in vowels:
                count +=1
        MaxCount  =count 

        for i in range(k,len(word)):
            if word[i-k] in vowels:
                count -=1
            
            if word[i] in vowels:
                count +=1
    
            MaxCount = max(MaxCount,count)
    
        return MaxCount
