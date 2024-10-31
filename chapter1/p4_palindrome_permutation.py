# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangment of letters. The palindrome does not need to be limited to just dictionary words.
import string
from collections import Counter

def clean_phrase(phrase):
    result = []
    for c in phrase.lower():
        if c in string.ascii_lowercase:
            result.append(c)
    return result

def permutazione_palindroma_pythonic(phrase):
    counter = Counter(clean_phrase(phrase))
    odd_count = 0
    for val in counter.values():
        if val % 2 == 1:
            odd_count += 1
    return odd_count <= 1

print(permutazione_palindroma_pythonic("Tact Coa"))