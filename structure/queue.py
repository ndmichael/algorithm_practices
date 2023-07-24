class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
s = Queue()
print(s.size())
print(s.isEmpty())
s.enqueue(5)
s.enqueue(4)
s.enqueue(3)
s.enqueue(2)
s.enqueue(1)
print(s.size())

