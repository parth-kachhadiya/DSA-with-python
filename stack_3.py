class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def append(self,data):
        node = Node(data,self.head)
        self.head = node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.head = self.head.next
            self.size -= 1
        else:
            print("Linked list is already empty..!")

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            return "Linked list is already empty..!"

    def is_empty(self):
        return self.head == None


obj = Stack()
obj.append(10)
obj.append(20)
obj.append(30)
print(obj.peek())
obj.pop()
print(obj.peek())
print(obj.size)
