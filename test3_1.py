import pickle


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def clear(self):
        self.items = []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
stack.clear()
print(stack.peek())


# 保存栈
with open('stack.pickle', 'wb') as file:
    pickle.dump(stack, file)

# 加载栈
with open('stack.pickle', 'rb') as file:
    loaded_stack = pickle.load(file)
