class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def append(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
            return
        if self.tail != None:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            return

    def prepend(self, data):
        new_node = node(data)
        new_node.next = self.head
        current_node = self.head

        if current_node == None:
            self.head = new_node
            self.tail = new_node
            self.head.next = new_node
            return

        if self.tail != None:
            self.tail.next = new_node
            new_node.next = self. head
            self.head = new_node
            return

    def length(self):
        current_node = self.head
        len = 0
        while current_node.next:
            len = len + 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return len

    def deletion_head(self):
        if self.head != None:
            next_node = self.head.next
            self.tail.next = next_node
            self.head = next_node
        else:
            print("Empty List")

    def deletion_tail(self):
        if self.head != None :
            current_node = self.head
            while current_node.next.next != self.head :
                current_node = current_node.next
            self.tail = current_node
            current_node.next = self.head
        return

    def traverse(self):
        if self.tail == None:
            print("The list is empty")
            return
        newNode = self.tail.next
        while newNode:
            print(newNode.data, end=" ")
            newNode = newNode.next
            if newNode == self.tail.next:
                break

list = CLL()
print()
list.append(100)
list.append(200)
list.append(300)
list.append(400)
list.traverse()
list.prepend(500)
print()
print()
list.traverse()
print()

list.deletion_head()
print()
list.traverse()
print()
print()




