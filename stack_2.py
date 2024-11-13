class Stack(list):
    
    def is_empty(self):
        return len(self) == 0

    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            print("Already empty.!")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            print("Already empty.!")

    def size(self):
        return len(self)

    def insert(self): # Restrict the use of 'insert' method which exists in parent class 'list'
        raise AttributeError("No attribute named 'insert'")

obj = Stack()
obj.insert()