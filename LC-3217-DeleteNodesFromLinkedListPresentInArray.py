# LeetCode Problem: 3217. Delete Nodes From Linked List Present In Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
        
            curr = curr.next
        
        return dummy.next