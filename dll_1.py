class Node:
    def __init__(self,data,previous = None,next = None):
        self.data = data
        self.previous = previous
        self.next = next

class DLL:
    def __init__(self,head = None):
        self.head = head

    def