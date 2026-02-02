# 225. Implement Stack Using Queues - Explanation

class MyStack:
  def __init__(self):
    self.q = deqeu()
  
  def push(self, x: int) -> None:
    self.q.append(x)
    for _ in range(len(self.q) - 1):
      self.q.append(self.q.popleft())
  
  def pop(self) -> int:
    return self.q.popleft()

  def top(self) -> int:
    return self.q[0]
  
  def empty(self) -> bool:
    return len(self.q) == 0