"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#itrate through the given linked list and create deep copy of the nodes without showing the next or random pointers and store it in hash map
        copy= {None:None} #handles the case where next or random pointer is Null/None
        
        cur = head
        while cur:
            copy[cur]= Node(cur.val)
            cur = cur.next

        
# now add .next and .random to the copy nodes while itrating through original linked list
        
        cur = head #reset pointer back to head
        while cur:
            copy[cur].next = copy[cur.next] #connects the node's next pointer to the exsisting node in the dict
            copy[cur].random = copy[cur.random] #connects the node's random pointer to the exsisting node in the dict
            cur= cur.next
        
        return copy[head]