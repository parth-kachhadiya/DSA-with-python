class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class SLL:
    """
    Index must be start with '1'
    """

    def __init__(self,head = None):
        self.head = head
        
    def is_empty(self):
        return self.head == None
    
    """ > - <> - <> - <> - <> - <> - <> - < Insert > - <> - <> - <> - <> - <> - <    """
    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_last(self,data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            iterator = self.head
            while iterator.next != None:
                iterator = iterator.next
            iterator.next = node

    def insert_at_index(self,data,index):
        n = self.lengh()
        if index > (n + 1) or index <= 0:
            print("Out of bound..")
        else:
            if index == 1:
                self.insert_at_begin(data)
            elif index == (n + 1):
                self.insert_at_last(data)
            else:
                iterator = self.head
                counter = 1
                while counter < (index-1) and iterator.next:
                    counter += 1
                    iterator = iterator.next
                node = Node(data,iterator.next)
                iterator.next = node


    """ > - <> - <> - <> - <> - <> - <> - < Update > - <> - <> - <> - <> - <> - < """
    def update_at_beginning(self,new_value):
        if not self.is_empty():
            self.head.data = new_value
        else:
            print("Linked list is already empty....!")

    def update_at_end(self, new_value):
        if not self.is_empty():
            iterator = self.head
            while iterator.next != None:
                iterator = iterator.next
            iterator.data = new_value
        else:
            print("Linked list is already empty....!")

    def update_at_index(self, new_data, index):
        n = self.lengh()
        if index > n or index <= 0:
            print("Index out of bound !!")
        else:
            if index == 1:
                self.update_at_beginning(new_data)
            elif index == n:
                self.update_at_end(new_data)
            else:
                counter = 1
                iterator = self.head
                while counter < index and iterator.next:
                    counter += 1
                    iterator = iterator.next
                iterator.data = new_data

    """ > - <> - <> - <> - <> - <> - <> - < Delete > - <> - <> - <> - <> - <> - < """
    def delete_at_beginning(self):
        if not self.is_empty():
            self.head = self.head.next
        else:
            print("Linked list is already empty")

    def delete_at_end(self):
        if not self.is_empty():
            if self.lengh() == 1:
                self.head = None
            else:
                iterator = self.head
                while iterator.next.next:
                    iterator = iterator.next
                iterator.next = iterator.next.next
        else:
            print("Linked list is already empty")

    def delete_at_index(self,index):
        n = self.lengh()
        if index <= 0 or index > n:
            print("Index out of bound")
        else:
            if index == 1:
                self.delete_at_beginning()
            elif index == n:
                self.delete_at_end()
            else:
                iterator = self.head
                counter = 1
                while counter < (index-1) and iterator.next:
                    counter += 1
                    iterator = iterator.next
                iterator.next = iterator.next.next

    """ > - <> - <> - <> - <> - <> - <> - < Helper functions > - <> - <> - <> - <> - <> - < """
    def lengh(self):
        iterator = self.head
        counter = 0
        while iterator:
            iterator = iterator.next
            counter += 1
        return counter

    def start_iteration(self):
        if self.is_empty():
            print("Linked list is already empty !!")
        else:
            iterator = self.head
            while iterator:
                print(f"{iterator.data},",end=' ')
                iterator = iterator.next
            print()

# Driver code
obj = SLL()