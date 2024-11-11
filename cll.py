class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class CLL:
    def __init__(self,head = None):
        self.head = head

    """ > - <> - <> - <> - <> - <> - <> - < Insert > - <> - <> - <> - <> - <> - < """
    def inser_at_beginning(self,data):
        node = Node(data)
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                iterator = iterator.next
            node.next = self.head
            self.head = node
            iterator.next = self.head
        else:
            self.head = node
            node.next = self.head

    def insert_at_end(self,data):
        node = Node(data)
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                iterator = iterator.next
            iterator.next = node
            node.next = self.head
        else:
            node.next = node
            self.head = node

    def insert_after_this(self,data,new_data):
        if self.is_empty():
            if flag := int(input("Linked list is already empty, do you want to insert new node [1/0]: ")):
                self.inser_at_beginning(new_data)
            else:
                return
        else:
            if self.head.data == data:
                self.inser_at_beginning(new_data)   
            else:
                iterator = self.head
                while iterator.next.data != data and iterator.next != self.head:
                    iterator = iterator.next
                if iterator.next == self.head and iterator.data != data:
                    print("No data found !!")
                elif iterator.next == self.head and iterator.data == data:
                    self.insert_at_end(new_data)
                else:
                    node = Node(new_data)
                    node.next = iterator.next
                    iterator.next = node

    """ > - <> - <> - <> - <> - <> - <> - < Update > - <> - <> - <> - <> - <> - < """
    def update_at_beginning(self,new_data):
        self.head.data = new_data if not self.is_empty() else print("Linked list is already empty..!")

    def update_at_end(self,new_data):
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                iterator = iterator.next
            iterator.data = new_data
        else:
            print("Linked list is already empty..!")

    def update_at_this(self,data,new_data):
        if not self.is_empty():
            if self.head.data == data:
                self.head.data = new_data
            else:
                iterator = self.head
                while iterator.data != data and iterator.next != self.head:
                    iterator = iterator.next
                iterator.data = new_data if iterator.data == data else iterator.data
        else:
            print("Linked list is already empty..!")

    """ > - <> - <> - <> - <> - <> - <> - < Delete > - <> - <> - <> - <> - <> - < """
    def delete_from_beginning(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                iterator = self.head
                while iterator.next != self.head:
                    iterator = iterator.next
                self.head = self.head.next
                iterator.next = self.head
        else:
            print("Linked list is already empty..!")

    def delete_from_end(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                iterator = self.head
                while iterator.next.next != self.head:
                    iterator = iterator.next
                iterator.next = self.head
        else:
            print("Linked list is already empty..!")

    def delete_to_this(self,data):
        if not self.is_empty():
            if self.head.data == data:
                self.delete_from_beginning()
            else:
                iterator = self.head
                while iterator.next.data != data and iterator.next != self.head:
                    iterator = iterator.next
                if iterator.next.data != data:
                    print("Node doesn't found..!")
                elif iterator.next.data == data and iterator.next.next == self.head:
                    iterator.next = self.head
                else:
                    iterator.next = iterator.next.next

        else:
            print("Linked list is already empty..!")

    """ > - <> - <> - <> - <> - <> - <> - < Helper functions > - <> - <> - <> - <> - <> - < """
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
            print("Linked list is alread empty..!")

obj = CLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.insert_at_end(50)
obj.start_iteration()
obj.delete_to_this(60)
obj.start_iteration()