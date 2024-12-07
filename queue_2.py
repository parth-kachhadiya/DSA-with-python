'''
Implement queue datastructure using singly linked list
'''

from sll_1 import Node

class Queue:
    def __init__(self,rear = None,front = None):
        self.rear = rear
        self.front = front

    def isEmpty(self):
        return self.front == None and self.rear == None
    
    def inQueue(self,data):
        node = Node(data)
        if not self.isEmpty():
            self.rear.next = node
            self.rear = node
        else:
            self.rear = node
            self.front = node

    def deQueue(self):
        if not self.isEmpty():
            if not self.front.next:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
        else:
            print("Already empty..!")

    def iteration(self):
        if not self.isEmpty():
            iterator = self.front
            while iterator:
                print(iterator.data,end=', ')
                iterator = iterator.next
            print()
        else:
            print("Already empty..!")

    def getRear(self):
        return self.rear.data if not self.isEmpty() else "Already empty..!"
    
    def getFront(self):
        return self.front.data if not self.isEmpty() else "Already empty..!"
    
    def getSize(self):
        if not self.isEmpty():
            ctr = 0
            iterator = self.front
            while iterator:
                iterator = iterator.next
                ctr += 1
            return ctr
        else:
            return 0

obj = Queue()
# obj.inQueue(10)
# obj.inQueue(20)
print(obj.getSize())