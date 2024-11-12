class Node:
    def __init__(self,data,previous=None,next=None):
        self.data = data
        self.previous = previous
        self.next = next

class DCLL:
    def __init__(self,head=None):
        self.head = head

    """ > - <> - <> - <> - <> - <> - <> - < Insert > - <> - <> - <> - <> - <> - < """
    def insert_at_begin(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = node.previous = self.head
        else:
            iterator = self.head
            while iterator.next != self.head:
                iterator = iterator.next
            iterator.next = node
            node.previous = iterator
            node.next = self.head
            self.head.previous = node
            self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                iterator = iterator.next
            iterator.next = node
            node.previous = iterator
            node.next = self.head
            self.head.previous = iterator
        else:
            self.head = node
            node.next = node.previous = self.head

    def insert_at_this(self,index,data):
        if not self.is_empty():
            pass
        else:
            self.insert_at_begin(data) if int(input("Linked list is already empty, do you want to insert node at first position [1/0]: ")) else print("Couldn't insert any node !")



    """ > - <> - <> - <> - <> - <> - <> - < Helper Functions > - <> - <> - <> - <> - <> - < """
    def is_empty(self):
        return self.head == None
    
    def start_iteration(self):
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                print(f"{iterator.data}, ",end=' ')
                iterator = iterator.next
            print(f"{iterator.data}")
        else:
            print("Linked list is already empty..!")

obj = DCLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.start_iteration()