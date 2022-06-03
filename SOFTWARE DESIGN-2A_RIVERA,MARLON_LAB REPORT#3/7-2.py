class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total = total + 1
            cur = cur.next
        return total

    def traverse(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def mergeList(self, L, M):
        res = None
        ref = res
        while (1):

            if L is None:
                ref = M
                break
            if M is None:
                ref = L
                break

        return res
                



#creating instance
my_list = linked_list()
my_list2 = linked_list()

print("")
my_list.append("100")
my_list.append("200")
my_list.append("300")
my_list.append("400")
my_list.traverse()
print("")

print("")

print("")
my_list2.append("500")
my_list2.append("600")
my_list2.append("700")
my_list2.append("800")
my_list2.traverse()
print("")

my_list.head = my_list.mergeList(my_list.head, my_list2.head)

print(my_list.traverse())