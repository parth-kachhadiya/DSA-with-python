'''
Queue datastructure with fixed size array container
'''

class Queue:
    def __init__(self):
        self.container = [None] * 10 
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == 9

    def inQueue(self,data):
        if not self.isFull():
            self.rear += 1
            self.container[self.rear] = data
        else:
            print("Already full..!")

    def deQueue(self):
        if not self.isEmpty():
            self.front += 1
            self.container[self.front] = None
        else:
            print("Already empty..!")

    def getFront(self):
        if not self.isEmpty():
            return self.container[self.front+1]
        else:
            print("Already empty..!")

    def getRear(self):
        if not self.isEmpty():
            return self.container[self.rear]
        else:
            print("Already empty..!")

    def iteration(self):
        if not self.isEmpty():
            for element in range(self.front,self.rear):
                print(f"{self.container[element+1]}, ",end=" ")
            print()
        else:
            print("Already empty..!")

    def getSize(self):
        return self.rear - self.front

obj = Queue()
obj.inQueue(1)
obj.inQueue(2)
obj.inQueue(3)
print(obj.getSize())