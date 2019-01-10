#
# Implementation of a singly linked list. Add a method called “getNum(n).
# getNum(n) should return the data item from the node in the nth spot in the list.
#

class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, node):

        if not self.head:
            self.head = node
            self.size += 1
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node
            self.size +=1

    def getSize(self):
        return self.size

    def printLL(self):
        mynode = self.head
        c = 0
        while mynode:
            c += 1
            print(mynode.data, c)
            mynode = mynode.nextNode

    def getNum(self, value):
        mynode = self.head
        c = 0
        while mynode:
            c += 1
            if (c == value):
                return mynode.data
            mynode = mynode.nextNode


