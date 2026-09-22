class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.k = k
        self.front = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1 + self.k) % self.k
        self.arr[self.front] = value
        self.size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        rear = (self.front + self.size) % self.k
        self.arr[rear] = value
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.size -= 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        rear = (self.front + self.size - 1) % self.k
        return self.arr[rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k