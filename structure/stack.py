class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    

s = Stack()
print(s.isEmpty())

s.push(3)
s.push(7)
s.push(4)
s.push(1)

print(s.pop())
print(s.pop())