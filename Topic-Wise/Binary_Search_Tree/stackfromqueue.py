from queue import Queue
from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = Queue(100)
        self.queue2 = Queue(100)
        
    def push(self, x: int) -> None:
        self.queue1.put(x)

    def pop(self) -> int:
        while not self.queue1.empty():
            ans = self.queue1.get()
            if not self.queue1.empty():
                self.queue2.put(ans)
        self.queue1 ,self.queue2 = self.queue2 , self.queue1
        return ans
    
    def top(self) -> int:
        while not self.queue1.empty():
            ans = self.queue1.get()
            self.queue2.put(ans)
        self.queue1 ,self.queue2 = self.queue2 , self.queue1
        return ans
        

    def empty(self) -> bool:
        return self.queue1.empty()


class MyStack1:

    def __init__(self):
        self.q = deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
            
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
