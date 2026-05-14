# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         start_node = None
#         if list1 and list2:
#             if (list1.val < list2.val):
#                 start_node = list1
#                 list1 = list1.next
#             else:
#                 start_node = list2
#                 list2 = list2.next
#         else:
#             start_node = list1 or list2
#             return start_node

#         current = start_node

#         while(list1 or list2):
#             if not list1:
#                 current.next = list2
#                 break
#             elif not list2:
#                 current.next = list1
#                 break
#             else:
#                 if (list1.val < list2.val):
#                     current.next = list1
#                     list1 = list1.next
#                 else:
#                     current.next = list2
#                     list2 = list2.next
#             current = current.next
#         return start_node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start_node = tail_node = ListNode()
        curr1 = list1
        curr2 = list2

        while (curr1 and curr2):
            if (curr1.val < curr2.val):
                tail_node.next = curr1
                curr1 = curr1.next
            else:
                tail_node.next = curr2
                curr2 = curr2.next
            tail_node = tail_node.next

        tail_node.next = curr1 or curr2
        return start_node.next

def build(values):
    dummy = ListNode()
    cur = dummy

    for v in values:
        cur.next = ListNode(v)
        cur = cur.next

    return dummy.next


def print_list(node):
    arr = []

    while node:
        arr.append(node.val)
        node = node.next

    print(arr)


print_list(Solution().mergeTwoLists(
    build([1, 2, 4]),
    build([1, 3, 4])
))

print_list(Solution().mergeTwoLists(
    build([]),
    build([])
))

print_list(Solution().mergeTwoLists(
    build([]),
    build([0])
))
