class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)
    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

class PriorityQueueLink:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        """Will check if the Priority Queue is empty or not"""
        return self.length == 0

    def insert(self, cargo):
        """Will produce a list in which the node that has
        the largest element will be the head and the last
        will be the smallest"""
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            self.head = self.last = node
        elif node.cargo > self.head.cargo:
            node.next = self.head
            self.head = node
        elif node.cargo < self.last.cargo:
            self.last.next = node
            self.last = node
        elif node.cargo < self.head.cargo and node.cargo > self.last.cargo:
            temp = self.head
            p = self.head.next
            while p != None:

                if p.cargo > node.cargo:
                    temp = temp.next
                    p = p.next
                break
            node.next = temp.next
            temp.next = node
        self.length = self.length + 1

    def remove(self):
        """The largest node will be removed first,
        which will cause self.length to update."""
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo

    def printList(self):
        """This will print out the Priority Queue as a list"""
        a = []
        b = self.head
        while b != None:
            a.append(b.cargo)
            b = b.next
        print(a)
    
    
    def selectionSort(self):
        """ This will look in the Priority Queue
        and sort each element into least to greatest"""  
        l = []
        q = self.head
        while q != None:
            l.append(q.cargo)
            q = q.next
        items = l
        for i in range(0, len(items)):
            positionOfMin = i
            for j in range(i + 1, len(items)):
                if items[j] < items[positionOfMin]:
                    positionOfMin = j

            temp = items[i]
            items[i] = items[positionOfMin]
            items[positionOfMin] = temp
        print(items)
