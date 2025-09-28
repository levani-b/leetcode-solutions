# LeetCode Problem: 83. Remove Duplicates From Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if not head:
            return head
        
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next