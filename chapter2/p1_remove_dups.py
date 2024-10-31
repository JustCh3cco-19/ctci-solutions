# Write code to remove duplicates from an unsorted linked list
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?
from linked_list import LinkedList

def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll

def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll

ll = LinkedList([1, 1, 2, 3, 3, 4])
print("Before removing duplicates:", ll)

# Rimuovi i duplicati
remove_dups(ll)
print("After removing duplicates:", ll)
