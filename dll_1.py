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

    def insert_at_end(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            
            iterator.next = node
            node.previous = iterator

    def insert_after_given_value(self,value,new_value):
        if not self.is_empty():
            iterator = self.head
            while iterator.data != value and iterator.next:
                iterator = iterator.next

            if iterator.data != value:
                print("No data found")
            else:
                node = Node(new_value)
                node.next = iterator
                node.previous = iterator.previous
                iterator.previous.next = node
                iterator.previous = node

        else:
            print("Linked list is already empty..!")

    """ > - <> - <> - <> - <> - <> - <> - < Update > - <> - <> - <> - <> - <> - <    """
    def update_at_begin(self,new_value):
        if not self.is_empty():
            self.head.data = new_value
        else:
            print("Linked list is already empty..!")

    def update_at_end(self,new_value):
        if not self.is_empty():
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            iterator.data = new_value
        else:
            print("Linked list is already empty..!")

    def update_at_given_value(self,value,new_value):
        if not self.is_empty():
            iterator = self.head
            while iterator.data != value and iterator.next:
                iterator = iterator.next

            if iterator.data != value:
                print("No data found")
            else:
                iterator.data = new_value
        else:
            print("Linked list is already empty..!")

    """ > - <> - <> - <> - <> - <> - <> - < Delete > - <> - <> - <> - <> - <> - < """
    def delete_from_first(self):
        if not self.is_empty():
            if self.head.next == None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.previous = None
        else:
            print("Linked list is already empty..!")

    def delete_from_end(self):
        if not self.is_empty():
            iterator = self.head
            if not iterator.next:
                self.head = None
            else:
                while iterator.next:
                    iterator = iterator.next
                iterator.previous.next = None
                iterator.previous = None
        else:
            print("Linked list is already empty..!")
            
    def delete_this_node(self,data):
        if not self.is_empty():
            iterator = self.head
            while iterator.data != data and iterator.next:
                iterator = iterator.next
            if iterator.data != data:
                print("Data doesn't exist")
            else:
                if not iterator.next and not iterator.previous: # If there is only one node
                    self.head = None
                elif iterator.previous and not iterator.next: # If the node is at the last position
                    iterator.previous.next = None
                    iterator.previous = None
                elif not iterator.previous and iterator.next: # If the node is at first position
                    self.head = self.head.next
                    self.head.previous = None
                else: # Between, at any position
                    iterator.previous.next = iterator.next
                    iterator.next.previous = iterator.previous

        else:
            print("Linked list is already empty..!")

    """ > - <> - <> - <> - <> - <> - <> - < Helper functions > - <> - <> - <> - <> - <> - < """
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
            print("Linked list is already empty")

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
obj.insert_at_begin(40)
obj.insert_at_begin(30)
obj.insert_at_begin(20)
obj.insert_at_begin(10)
obj.start_iteration_from_begin()
obj.delete_this_node(50)
obj.start_iteration_from_begin()