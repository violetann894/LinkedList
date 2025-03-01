import timeit

setUp = """
class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:

    def __init__(self, head):
        self.head = head

    def listSearch(L, k):
        x = L.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def listPrepend(L, k):
        x = Node(k)
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
        while x is not None:
            print(x.key)
            x = x.next"""

if __name__ == "__main__":

    testListSearch= """linkList = LinkedList(None)
for i in range(0, 21):
    linkList.listPrepend(i)
linkList.listSearch(7)"""

    testListInsert= """linkList = LinkedList(None)
for i in range(0, 21):
    linkList.listPrepend(i)
linkList.listInsert(Node(8), linkList.listSearch(14))"""

    testListPrepend = """linkList = LinkedList(None)
for i in range(0, 21):
    linkList.listPrepend(i)
linkList.listPrepend(100)"""

    testListDelete= """linkList = LinkedList(None)
for i in range(0, 21):
    linkList.listPrepend(i)
linkList.listDelete(linkList.listSearch(14))"""

    print("Time for listSearch: ", timeit.timeit(setup = setUp, stmt = testListSearch, number=100000))
    print("Time for listInsert: ", timeit.timeit(setup=setUp, stmt=testListPrepend, number=100000))
    print("Time for listPrepend: ", timeit.timeit(setup=setUp, stmt=testListPrepend, number=100000))
    print("Time for listDelete: ", timeit.timeit(setup=setUp, stmt=testListDelete, number=100000))