# Implement an algorithm to delete a node in the middle (any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
# EXAMPLE-> Input: the node c from the linked list a->b->c->d->e->f
# Output: nothing is returned, but the new linked list looks like a->b->d->e->f
from linked_list import LinkedList

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)