class ListNode:
  def __init__(self, val):
    self.val = val # data
    self.next = None # pointer ke node setelahnya
    self.prev = None # pointer ke node sebelumnya

# implementation for Doubly Linke. List
class LinkedList:
  def __init__(self):
    # init the list within dummy head and tail nodes which makes
    # edge cases for insert and remove easier
    self.head = ListNode(-1) # dummy head
    self.tail = ListNode(-1) # dummy tail
    self.head.next = self.tail
    self.tail.prev = self.head
  
  # before head <-> A <-> B <-> tail
  # after head <-> X <-> A <-> B <-> tail
  def insertFront(self, val):
    newNode = ListNode(val)
    newNode.prev = self.head
    newNode.next = self.head.next

    self.head.next.prev = newNode
    self.head.next = newNode
    # proses
    # newNode.prev = head
    # newNode.next = head.next
    # node lama pertama (A) → prev = newNode
    # head.next = newNode
  
  # before head <-> A <-> B <-> tail
  # after head <-> A <-> B <-> X <-> tail
  def insertEnd(self, val):
    newNode = ListNode(val)
    newNode.next = self.tail
    newNode.prev = self.tail.prev

    self.tail.prev.next = newNode
    self.tail.prev = newNode
    # proses
    # new.prev = node terakhir
    # new.next = tail
    # node terakhir → next = new
    # tail.prev = new
  
  # remove first node after dummy head (assume it exists)
  # before head <-> A <-> B <-> tail
  # after head <-> B <-> tail
  def removeFront(self):
    self.head.next.next.prev = self.head
    self.head.next = self.head.next.next
    # proses
    # A dilewati
    # B.prev diubah ke head
    # head.next langsung ke B
  
  # remove last node before dummy tail (assume it exists)
  # before head <-> A <-> B <-> tail
  # after head <-> A <-> tail
  def removeEnd(self):
    self.tail.prev.prev.next = self.tail
    self.tail.prev = self.tail.prev.prev
    # proses
    # B dilewati
    # A.next = tail
    # tail.prev = A
  
  def print(self):
    curr = self.head.next
    while curr != self.tail:
      print(curr.val, " -> ")
      curr = curr.next
    print()