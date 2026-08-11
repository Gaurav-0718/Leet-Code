class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(","{","["]
        pair = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == pair[i]:
                        stack.pop()
                    else:
                        return False
        return len(stack)==0
