class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class stack:
    def __init__(self):
            self.data = []

    def push(self, data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()
    def size(self):
        return len(self.data)
    def isEmpty(self):
        if len(self.data) == 0:
            return False
        else:
            return True   
    def peek (self):
        return self.data[len(self.data) -1]


class queue:
    def _init_(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data ):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.count += 1
  
    def dequeue(self):
        curr = self.head.next
        curr.prev = None
        self.head = curr
        
    def size(self):
        return self.count 

    def isEmpty(self):
        if self.count == 0:
            return False
        else:
            return True
        

    def peek (self):
        return self.head
    

def isPalindrome (str):
    pass

yellow = input ('Enter string of choice: ')
print (isPalindrome(yellow))
