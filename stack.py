class Stack:
    def __init__(self):
        self.__container = []

    def is_empty(self):
        return len(self.__container) == 0
    
    def push(self,data):
        self.__container.append(data)

    def pop(self):
        if not self.is_empty():
            return self.__container.pop()
        else:
            raise IndexError("Stack is alread empty..!")
        
    def peek(self):
        if not self.is_empty():
            return self.__container[-1]
        else:
            raise IndexError("Stack is already empty..!")
        
    def size(self):
        counter = 0
        for _ in self.__container:
            counter += 1
        return counter
    
    def iteration(self):
        if not self.is_empty():
            print("--------")
            for elements in self.__container[::-1]:
                print(f"   {elements}\n--------")
        else:
            raise IndexError("Linked list is already empty.!")

obj = Stack()
