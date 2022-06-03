class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size = self.size + 1

    def traverse(self):
        element = []
        if self.tail == None:
            print("The list is empty")
            return
        current_node = self.head
        while current_node:
            element.append(current_node.data)
            current_node = current_node.next
        print(element)



    def deletion(self, data):
        if self.size == 1:
            print("There should be atleast two data in the list")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        elif self.size > 1:
            current_node = self.head
            previous_node = None
            while current_node:
                if current_node.data == data:
                    #removing the head node
                    if not previous_node:
                        next_node = current_node.next
                        next_node.prev = None
                        current_node.next = None
                        del current_node
                        self.head = next_node
                    #removing tail node
                    elif not current_node.next:
                        previous_node.next = None
                        current_node.prev = None
                        del current_node
                        self.tail = previous_node
                    #removing random element
                    else:
                        next_node = current_node.next
                        current_node.prev = None
                        current_node.next = None
                        del current_node
                        previous_node.next = next_node
                        next_node.prev = previous_node
                    self.size -= 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

#creating instance
List = DLL()

#appending the data
print("")
List.append(100)
List.append(200)
List.append(300)
List.append(400)
List.traverse()

print("")
List.deletion(200)
List.traverse()

print("")

