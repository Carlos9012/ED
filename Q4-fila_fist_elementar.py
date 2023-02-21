from array import array


EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

class EmptyQueueError(Exception):
    ...


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next: Node

    def __repr__(self) -> str:
        return f'{self.value}'

    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)


class Queue:

    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0

    def insert(self, node_value=None):
        new_node = Node(node_value)

        if not self.first:
            self.first = new_node

        if not self.last:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self._count += 1

    def remove(self) -> Node:
        if not self.first:
            raise EmptyQueueError('Empty Queue')

        first = self.first

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)

        self._count -= 1
        return first

    def __next__(self):
        try:
            next_value = self.pop()
            return next_value
        except EmptyQueueError:
            raise StopIteration
    
    

    def __repr__(self) -> str:
        if not self.first:
            return 'Queue()'
        return f'Queue({self.last})'


    def initByArray(self, array=None):
        if array is None or len(array) == 0:
            self.data = None
            self.next = None
        
        else:
            self.data = array[0]
        
            P = Queue()
            P.initByArray(array[1:])
        if P.data is not None:
            self.next = P

    def toArray(self, array=[]):
        if self is None:
            return

        array.append(self.data)

        if self.next is not None and self.next.data is not None:
            self.next.toArray(array)

        return array

    def print(self):
        array = self.toArray([])
        print(array)

    def fist(self, pfist=None):
        pri = self.first
        pfist = queue.remove()
        queue.insert(pfist)
        if not pri:
            return ''
        print(queue.last)
        
        return f'O primeiro item é: {pfist}'


if __name__ == "__main__":
    queue = Queue()
    queue.insert('A')
    queue.insert('B')
    queue.insert('C')
    print(queue.fist())
