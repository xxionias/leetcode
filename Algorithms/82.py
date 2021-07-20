"""
case 1: empty
None
=>
None

case 2: one node
1 -> None
=>
1 -> None

case 3: two duplicates
1 -> 1
=>
None

case 4: two duplicates + one single
1 -> 1 -> 2
=>
2 -> None

case 5: two duplicates + two duplicates
1 -> 1 -> 2 -> 2 -> None
=>
None

case 6: no duplicates
1 -> 2 -> 3 -> None
=>
1 -> 2 -> 3 -> None

Algo:
Inititate a dummy node and also a prev node whose `next` field points to the head
Initiate a curr node that points to the head
while curr node is not null:
    if curr.next and curr.next.val == curr.val:
        while curr.next and curr.next.val == curr.val:
            curr = curr.next
        prev.next = curr.next
    else:
        prev = prev.next
    curr = curr.next

Return dummy node's next
"""
class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def removeDuplicates(self, head):
        dummy = prev = Node(-1, head)
        curr = head
        while curr:
            if curr.next and curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next

def printNodes(head):
    while head:
        print(head.val)
        head = head.next
    return


# case 1
print("Case 1")
n0 = None
sol1 = Solution()
head1 = sol1.removeDuplicates(n0)
printNodes(head1)

# case 2
print("Case 2")
n1 = Node(1)
sol2 = Solution()
head2 = sol2.removeDuplicates(n1)
printNodes(head2)

# case 3
print("Case 3")
n1 = Node(1)
n2 = Node(1)
n1.next = n2
sol3 = Solution()
head3 = sol3.removeDuplicates(n1)
printNodes(head3)

# case 4
print("Case 4")
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n1.next = n2
n2.next = n3
sol4 = Solution()
head4 = sol4.removeDuplicates(n1)
printNodes(head4)

# case 5
print("Case 5")
n1 = Node(1)
n2 = Node(1)
n3 = Node(2)
n4 = Node(2)
n1.next = n2
n2.next = n3
n3.next = n4
sol5 = Solution()
head5 = sol5.removeDuplicates(n1)
printNodes(head5)



# case 6
print("Case 6")
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

sol6 = Solution()
head6 = sol6.removeDuplicates(n1)
printNodes(head6)
