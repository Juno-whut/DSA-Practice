import unittest


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = self.head
        self.size = 0


    # method insert first O(1)
    def insertFirst(self, value):
        if not self.head:
            self.head = Node(value, None)
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = Node(value, None)
            self.head.next = self.tail
        else:
            temp = self.head
            self.head = Node(value, temp)
        self.size += 1
            

    # method insert last O(1)
    def insertLast(self, value):
        if not self.tail:
            self.head = Node(value, None)
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = Node(value, None)
            self.head.next = self.tail
        else:
            temp = self.tail
            self.tail = Node(value, temp)
        self.size += 1


    # method insert at specific index O(n)
    def insert(self, value, index):
        p_node = None
        node = self.head
        count = 0
        if index < 0 or index > self.size:
            raise IndexError("Index out of Range")
        
        for node in range(index):
            if count == index-1:
                p_node = node
            if count == index:
                new_node = Node(value, node)
                p_node.next = new_node
            count += 1
            node = node.next
        self.size += 1   
        

    # remove first O(1)
    def removeHead(self):
        if not self.head:
            raise Exception("List is Empty")
        
        re_value = self.head
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return re_value


    # remove last O(n)
    def removetail(self):
        if not self.tail:
            raise Exception("List is Empty")
        
        self.size -= 1
        tail = self.tail
        node = self.head
        prev = self.head
        for i in range(self.size):
            if node == self.tail:
                self.tail = prev
            prev = node 
            node = node.next
        return tail
        

    # remove value at specific index O(n)
    def remove(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of Range")
        
        node = self.head
        prev = node
        for i in range(index):
            if i == index:
                value = prev.next.data
                prev.next = node.next
            prev = node 
            node = node.next
        self.size -= 1
        return value


    # method return value at certain position O(n)
    def lookupValue(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of Range")
        
        node = self.head 
        for i in range(index):
            if i == index:
                return node.data
            node = node.next


    # method return index of specific value O(n)
    def lookupIndex(self, value):
        if not self.head:
            raise Exception("List is Empty")
        
        node = self.head 
        for i in range(self.size):
            if node.data == value:
                return i 
            node = node.next
          
        raise Exception("Value not in List")


    # method return list of nodes in linked list O(n)
    def getList(self):
        if not self.head:
            return []
        
        relist = []
        node = self.head
        for i in range(self.size):
            relist.append(node.data)
            node = node.next
        return relist 
    

    # method print nodes in order O(n)
    def printLL(self):
        if not self.head:
            raise Exception("List is Empty")
        
        node = self.head
        for i in range(self.size):
            print(node.data)
            node = node.next


    # method print head O(1)
    def printHead(self):
        if not self.head:
            raise Exception("List is Empty")
        print(self.head.data)


    # method print tail O(1)
    def printTail(self):
        if not self.tail:
            raise Exception("List is Empty")
        print(self.tail.data)


    # method return head value O(1)
    def getHead(self):
        if not self.head:
            raise Exception("List is Empty")
        return self.head.data
    

    # method return tail value O(1)
    def getTail(self):
        if not self.tail:
            raise Exception("List is Empty")
        return self.tail.data
    

    # method remove duplicates O(n) time and O(n) space
    def remDuplicates(self):
        if not self.head:
            raise Exception("List is Empty")
        if not self.head.next:
            return "Removed 0 duplicates"
        
        duplicates = set()
        rmd = 0
        node = self.head
        prev = self.head
        for i in range(self.size):
            if node.data in duplicates:
                rmd += 1 
                prev.next = node.next
                self.size -= 1
            else:
                duplicates.add(node.data)
                prev = node 
                node = node.next
        return f"Removed {rmd} duplicates"


    # method get length O(1)
    def getLength(self):
        return self.size



class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
    
    def testInsertFirst(self):
        self.ll.insertFirst(1)
        self.assertEqual(self.ll.getHead(), 1)
        self.assertEqual(self.ll.getTail(), 1)
        self.assertEqual(self.ll.getLength(), 1)

    def testInsertLast(self):
        self.ll.insertLast(1)
        self.ll.insertLast(2)
        self.assertEqual(self.ll.getHead(), 1)
        self.assertEqual(self.ll.getTail(), 2)
        self.assertEqual(self.ll.getLength(), 2)

    def testInsert(self):
        self.assertRaises(IndexError, self.ll.insert, 1, -1)
        self.assertRaises(IndexError, self.ll.insert, 1, 3)
        self.ll.insert(1, 0)
        self.ll.insert(2, 1)
        self.ll.insert(3, 2)
        self.assertEqual(self.ll.getHead(), 1)
        self.assertEqual(self.ll.getTail(), 3)
        self.assertEqual(self.ll.getLength(), 3)

    def testRemoveHead(self):
        self.assertRaises(Exception, self.ll.removeHead)
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.removeHead().data, 3)
        self.assertEqual(self.ll.removeHead().data, 2)
        self.assertEqual(self.ll.removeHead().data, 1)
        self.assertEqual(self.ll.getLength(), 0)

    def testRemoveTail(self):
        self.assertRaises(Exception, self.ll.removetail)
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.removetail().data, 1)    
        self.assertEqual(self.ll.removetail().data, 2)
        self.assertEqual(self.ll.removetail().data, 3)
        self.assertEqual(self.ll.getLength(), 0)

    def testRemove(self):
        self.assertRaises(IndexError, self.ll.remove, -1)
        self.assertRaises(IndexError, self.ll.remove, 3)
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.remove(0).data, 3)
        self.assertEqual(self.ll.remove(1).data, 2)
        self.assertEqual(self.ll.remove(0).data, 1)
        self.assertEqual(self.ll.getLength(), 0)

    def testAllPrint(self):
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.getList(), [3, 2, 1])
        self.assertEqual(self.ll.printHead(), 3)
        self.assertEqual(self.ll.printTail(), 1)

    def testDuplicates(self):
        self.ll.insertFirst(1)
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.remDuplicates(), "Removed 2 duplicates")
        self.assertEqual(self.ll.getLength(), 3)

    def testAllGet(self):
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.getHead(), 3)
        self.assertEqual(self.ll.getTail(), 1)
        self.assertEqual(self.ll.getLength(), 3)

    def testLookUP(self):
        self.ll.insertFirst(1)
        self.ll.insertFirst(2)
        self.ll.insertFirst(3)
        self.assertEqual(self.ll.lookupIndex(3), 0)
        self.assertEqual(self.ll.lookupIndex(2), 1)
        self.assertEqual(self.ll.lookupIndex(1), 2)
        self.assertRaises(Exception, self.ll.lookupIndex, 4)
        self.assertEqual(self.ll.lookupValue(0), 3)
        self.assertEqual(self.ll.lookupValue(1), 2)
        self.assertEqual(self.ll.lookupValue(2), 1)



if __name__ == '__main__':
    unittest.main()