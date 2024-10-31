# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

from linked_list import LinkedList

def somma_liste(ll_a, ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = NumericLinkedList()
    resto = 0
    while n1 or n2:
        risultato = resto
        if n1:
            risultato += n1.value
            n1 = n1.next
        if n2:
            risultato += n2.value
            n2 = n2.next
        
        ll.add(risultato % 10)
        resto = risultato // 10
    
    if resto:
        ll.add(resto)
    
    return ll


class NumericLinkedList(LinkedList):
    def __init__(self, values=None):
        """handle integer as input"""
        if isinstance(values, int):
            values = [int(c) for c in str(values)]
            values.reverse()
        elif isinstance(values, list):
            values = values.copy()

        super().__init__(values)

    def numeric_value(self):
        number = 0
        for place, node in enumerate(self):
            number += node.value * 10**place
        return number