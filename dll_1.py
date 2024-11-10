class Node:
    def __init__(self,data,previous = None,next = None):
        self.data = data
        self.previous = previous
        self.next = next

class DLL:
    def __init__(self,head = None):
        self.head = head

    """ > - <> - <> - <> - <> - <> - <> - < Insert > - <> - <> - <> - <> - <> - <    """
    def insert_at_begin(self,data):
        node = Node(data,next=self.head)
        if not self.is_empty():
            self.head.previous = node
        self.head = node

    def is_empty(self):
        return self.head == None

    def start_iteration_from_begin(self):
        if not self.is_empty():
            iterator = self.head
            while iterator:
                print(f"{iterator.data}, ",end=' ')
                iterator = iterator.next
            print()
        else:
            print("Linked list is already empty..!")

    def start_iteration_from_end(self):
        if not self.is_empty():
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            
            while iterator:
                print(f"{iterator.data}, ",end=' ')
                iterator = iterator.previous
            print()
        else:
            print("Linked list is already empty..!")

obj = DLL()
obj.start_iteration_from_begin()
obj.insert_at_begin(30)
obj.insert_at_begin(20)
obj.insert_at_begin(10)
obj.start_iteration_from_end()