class Node:

    """The constructor for the Node class creates a new Node object that holds information about the current state
        of the Node.
        key - The data that the Node needs to hold
        next - The pointer to the next object, starts as none because nothing is connected to a newly created Node
        """
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:

    """The constructor for the LinkedList class creates a new LinkedList object.
        head - The Node at the beginning of the list"""
    def __init__(self, head):
        self.head = head

    """listSearch accepts a key value for a Node in the LinkedList and returns if the Node was found.
        k - The key value for the desired Node
        
        Return x - The Node with the key value given, returns none if the Node was not found"""
    def listSearch(L, k):
        x = L.head
        while x is not None and x.key != k:
            x = x.next
        return x

    """listPrepend accepts a key value for a Node, creates a new Node object and adds it to the beginning of the 
        linked list.
        k - The key value for the new head Node"""
    def listPrepend(L, k):
        x = Node(k)
        x.next = L.head
        x.prev = None
        if L.head is not None:
            L.head.prev = x
        L.head = x

    """listInsert inserts a Node after a chosen Node.
        x - The Node to be inserted after y
        y - The Node that x will be inserted after"""
    def listInsert(L, x, y):
        x.next = y.next
        x.prev = y
        if y.next is not None:
            y.next.prev = x
        y.next = x

    """listDelete deletes the desired node in the linked list.
        x - The Node object to be deleted from the list"""
    def listDelete(L, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            L.head = x.next
            if x.next is not None:
                x.next.prev = x.prev

    """printLinkedList prints out the key values of the linked list, with the value at the top being the 
        key value of the head of the list."""
    def printLinkedList(L):
        x = L.head
        while x is not None:
            print(x.key)
            x = x.next

if __name__ == "__main__":

    """Adding Nodes to the linked list"""
    linkList = LinkedList(Node(1))
    linkList.listPrepend(2)
    linkList.listPrepend(3)
    linkList.listPrepend(4)
    linkList.listPrepend(5)

    """Testing the printLinkedList method"""
    print("Printing out the linked list")
    linkList.printLinkedList()
    print()

    newNode = Node(6)

    """Testing the listInsert and the listSearch method"""
    linkList.listInsert(newNode, linkList.listSearch(3))
    print("Printing out the linked list after inserting a new node")
    linkList.printLinkedList()
    print()

    """Testing the listDelete method"""
    linkList.listDelete(linkList.listSearch(2))
    print("Printing out the linked list after deleting a node")
    linkList.printLinkedList()
    

    
    
