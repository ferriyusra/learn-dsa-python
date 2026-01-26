# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]
# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []
# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[listNode]:
    
    dummy = node = ListNode()

    # list1 → 1 → 2 → 4 → null
    # list2 → 1 → 3 → 5 → null

    # dummy → null
    # node  ↑

    while list1 and list2:

      # iteration 1
      # list1.val = 1
      # list2.val = 1
      # dummy → 1 → null
      # node        ↑
      # list1 → 1 → 2 → 4 → null
      # list2 → 3 → 5 → null
      # get from list2 because the condition else
      # node.next = list2
      # list2 = list2.next
      # node = node.next

      # iteration 2
      # 1 < 3
      # get from list1
      # dummy → 1 → 1 → null
      # node             ↑
      # list1 → 2 → 4 → null
      # list2 → 3 → 5 → null

      # iteration 3
      # 2 < 3
      # get from list1
      # dummy → 1 → 1 → 2 → null
      # node                  ↑
      # list1 → 4 → null
      # list2 → 3 → 5 → null


      # iteration 4
      # 4 < 3
      # dummy → 1 → 1 → 2 → 3 → null
      # node                       ↑
      # list1 → 4 → null
      # list2 → 5 → null

      # iteration 5
      # 4 < 5
      # dummy → 1 → 1 → 2 → 3 → 4 → null
      # node                            ↑
      # list1 → null
      # list2 → 5 → null

      if list1.val < list2.val:
        node.next = list1
        list1 = list.next
      else:
        node.next = list2
        list2 = list2.next
      node = node.next
    
    # loop stop becase
    # list1 == null

    node.next = list1 or list2
    # dummy → 1 → 1 → 2 → 3 → 4 → 5 → null


    return dummy.next
    # 1 → 1 → 2 → 3 → 4 → 5 → null
