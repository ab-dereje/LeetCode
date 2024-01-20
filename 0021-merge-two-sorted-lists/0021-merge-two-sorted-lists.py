# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        current = dummy

        # Pointers to the current nodes in list1 and list2
        p1, p2 = list1, list2

        # Iterate until either list1 or list2 is exhausted
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                # Append the current node from list1 to the merged list
                current.next = p1
                # Move the pointer in list1 to the next node
                p1 = p1.next
            else:
                # Append the current node from list2 to the merged list
                current.next = p2
                # Move the pointer in list2 to the next node
                p2 = p2.next

            # Move the pointer in the merged list to the next node
            current = current.next

        # If there are remaining nodes in list1, append them to the merged list
        if p1 is not None:
            current.next = p1

        # If there are remaining nodes in list2, append them to the merged list
        if p2 is not None:
            current.next = p2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next

# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list
while merged_list is not None:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
