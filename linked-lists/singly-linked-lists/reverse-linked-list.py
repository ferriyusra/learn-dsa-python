# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def reverseList(self,head):
    prev, curr = None, head
    # prev = None
    # # curr = 0 → 1 → 2 → 3 → null

    while curr:
      
      # iteration 1
      # temp = curr.next      # temp = 1
      # curr.next = prev      # 0 → null
      # prev = curr           # prev = 0
      # curr = temp           # curr = 1
      # prev: 0 → null
      # curr: 1 → 2 → 3 → null

      # iteration 2
      # temp = 2
      # 1.next = 0
      # prev = 1
      # curr = 2
      # prev: 1 → 0 → null
      # curr: 2 → 3 → null

      # iteration 3
      # temp = 3
      # 2.next = 1
      # prev = 2
      # curr = 3
      # prev: 2 → 1 → 0 → null
      # curr: 3 → null

      # iteration 3
      # temp = null
      # 3.next = 2
      # prev = 3
      # curr = null
      # prev: 2 → 1 → 0 → null
      # curr: 3 → null

      # iteration 4
      # prev: 2 → 1 → 0 → null
      # curr: 3 → null
      # temp = null
      # 3.next = 2
      # prev = 3
      # curr = null
      # prev: 3 → 2 → 1 → 0 → null
      # curr: null (stop)

      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev