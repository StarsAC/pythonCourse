class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def peek(self):
        if not self.is_empty():
            return self.items[0], self.items[-1]
        else:
            print("Queue is empty")
            return None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.peek())
print(type(queue.peek()))