class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque()

        for i in range(len(tickets)):
            front = q.append(i)
        
        turn = 0

        while tickets[k] > 0 :
            front = q.popleft()

            tickets[front] -=1

            if tickets[front] > 0:
                q.append(front)
            
            turn +=1

        return turn