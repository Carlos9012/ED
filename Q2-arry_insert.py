from typing import Deque, Any
from collections import deque

queue: Deque[Any] = deque()
queue.insert(0,"A")
print(queue)
queue.insert(1,"B")
print(queue)
queue.insert(2,"C")
print(queue)
