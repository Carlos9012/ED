from typing import Deque, Any
from collections import deque

queue: Deque[Any] = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)
