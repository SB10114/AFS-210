class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            # print(val)
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node = Node(data)
        
        if self.count == 0:
            self.head = node
            self.tail = node 
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node        
        self.count += 1
   
    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node(data)
        
        if self.count == 0:
            self.tail = node
            self.head = node
             
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1
    
    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.

        if index == self.count:
            return self.addLast(data) 
        elif index == 0:
            return self.addFirst(data)
        elif index > self.count:
            return 
        else:
            curr = self.head
            pos = 0
            node = Node(data)
            while curr != None:
                if(pos == index):
                    curr.prev.next = node 
                    node.prev = curr.prev
                    curr.next = curr
                    curr.prev = node
                    break
                pos += 1
                curr = curr.next
        self.count += 1
    
    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        curr = self.head
        pos = -1
        
        while curr.next != None:
            pos += 1
            if(curr.data == data):
                return pos
            curr = curr.next
        return -1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next.prev = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

list = DoublyLinkedList()

list.addFirst("May")
list.add("the")
list.add("force")
list.add("be")
list.add("with")
list.add("you")
print(list)
print(list.indexOf("with"))
list.delete("you")
list.addAtIndex("us", 5)
list.addAtIndex("all", 6)
list.addAtIndex("!", 7)
print(list)