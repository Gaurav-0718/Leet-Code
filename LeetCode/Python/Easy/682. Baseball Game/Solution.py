class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i not in ["C","D","+"]:
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                value = stack[-1]*2
                stack.append(value)
            else:
                value = stack[-1]+stack[-2]
                stack.append(value)
        ans = sum(stack)

        return ans