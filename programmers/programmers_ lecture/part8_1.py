class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        curr = self.getAt(pos)

        if self.nodeCount == 1:
            self.head = None
            self.tail = None

        else:
            if pos == 1:
                self.head = curr.next
            elif pos == self.nodeCount:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
        self.nodeCount -= 1
        return curr.data          



    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
linked_list = LinkedList()
linked_list.insertAt(1,a)
linked_list.insertAt(2,b)
linked_list.insertAt(3,c)
linked_list.insertAt(4,d)
print(linked_list.traverse())
print()
print()
print(linked_list.popAt(1))
print(linked_list.traverse())
# print(linked_list.popAt(2))
# print(linked_list.traverse())
# print(linked_list.popAt(3))
# print(linked_list.traverse())
# print(linked_list.popAt(4))
# print(linked_list.traverse())