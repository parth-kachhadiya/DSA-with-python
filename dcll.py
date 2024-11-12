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
            self.head.previous = node
        else:
            self.head = node
            node.next = node.previous = self.head

    def insert_at_this(self,index,data):
        n = self.length()
        if not self.is_empty():
            if index <= 0 or index > (n + 1):
                print("Index outof bound..!")
            elif index == 1:
                self.insert_at_begin(data)    
            elif index == (n + 1):
                self.insert_at_end(data)
            else:
                node = Node(data)
                iterator = self.head
                counter = 1
                while (counter + 1) != index:
                    iterator = iterator.next
                    counter += 1
                node.next = iterator.next
                node.next.previous = node
                iterator.next = node
                node.previous = iterator
        else:
            self.insert_at_begin(data) if int(input("Linked list is already empty, do you want to insert node at first position [1/0]: ")) else print("Couldn't insert any node !")

    """ > - <> - <> - <> - <> - <> - <> - < Update > - <> - <> - <> - <> - <> - < """
    def update_at_beginning(self,new_data):
        if not self.is_empty():
            self.head.data = new_data
        else:
            print("Linked list is already empty..!")

    def update_at_last(self,new_data):
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                iterator = iterator.next
            iterator.data = new_data
        else:
            print("Linked list is already empty..!")

    def update_at_this(self, old_data, new_data):
        if not self.is_empty():
            iterator = self.head
            while iterator.data != old_data and iterator.next != self.head:
                iterator = iterator.next
            if iterator.next == self.head and old_data != iterator.data:
                print("No data found..!")
            else:
                iterator.data = new_data
        else:
            print("Linked list is already empty..!")

    """ > - <> - <> - <> - <> - <> - <> - < Delete > - <> - <> - <> - <> - <> - < """
    def delete_from_first(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                iterator = self.head
                while iterator.next != self.head:
                    iterator = iterator.next
                iterator.next = self.head.next
                self.head = iterator.next
                self.head.previous = iterator
        else:
            print("Linked list is already empty..!")

    def delete_from_last(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                iterator = self.head
                while iterator.next != self.head:
                    iterator = iterator.next
                iterator.previous.next = self.head
                self.head.previous = iterator.previous
        else:
            print("Linked list is already empty..!")

    def delete_this(self,data):
        if not self.is_empty():
            if self.head.data == data:
                self.delete_from_first()
            else:
                iterator = self.head
                while iterator.next != self.head and data != iterator.data:
                    iterator = iterator.next
                if iterator.next == self.head and iterator.data == data:
                    self.delete_from_last()
                elif iterator.data == data:
                    iterator.previous.next = iterator.next
                    iterator.next.previous = iterator.previous
                else:
                    print("No data found..!")
        else:
            print("Linked list is already empty..!")


    """ > - <> - <> - <> - <> - <> - <> - < Helper Functions > - <> - <> - <> - <> - <> - < """
    def is_empty(self):
        return self.head == None
    
    def start_iteration_from_beginning(self):
        if not self.is_empty():
            iterator = self.head
            while iterator.next != self.head:
                print(f"{iterator.data}, ",end=' ')
                iterator = iterator.next
            print(f"{iterator.data}")
        else:
            print("Linked list is already empty..!")

    def start_iteration_from_last(self):
        if not self.is_empty():
            iterator = self.head.previous
            while iterator != self.head:
                print(f"{iterator.data}, ",end=' ')
                iterator = iterator.previous
            print(iterator.data)
        else:
            print("Linked list is already empty..!")

    def length(self):
        if self.is_empty():
            return 0
        else:
            iterator = self.head
            counter = 1
            while iterator.next != self.head:
                iterator = iterator.next
                counter += 1
            return counter

obj = DCLL()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.start_iteration_from_last()