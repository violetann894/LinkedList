class Node:

    def __init__(self, data, pointer):
        self.key = data
        self.next = pointer
        self.prev = None


class LinkedList:

    def __init__(self, head):
        self.head = head

    def listSearch(L, k):
        x = L.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def listPrepend(L, k):
        x = Node(k, None)
        x.next = L.head
        x.prev = None
        if L.head is not None:
            L.head.prev = x
        L.head = x

    def listInsert(L, x, y):
        x.next = y.next
        x.prev = y
        if y.next is not None:
            y.next.prev = x
        y.next = x

    def listDelete(L, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            L.head = x.next
            if x.next is not None:
                x.next.prev = x.prev

    def printLinkedList(L):
        x = L.head
        while x.next is not None:
            print(x.key)
            x = x.next

if __name__ == "__main__":
    
    linkList = LinkedList(Node(1, None))
    linkList.listPrepend(2)
    linkList.printLinkedList()
    print()
    linkList.listPrepend(3)
    linkList.printLinkedList()
    print()
    linkList.listPrepend(4)
    linkList.printLinkedList()
    print()
    linkList.listPrepend(5)
    linkList.printLinkedList()
    print()
 

    

    
    
