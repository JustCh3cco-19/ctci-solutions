# Given two strings, write a method to decide if one is a permutation of the other.
from collections import Counter

def trova_permutazione(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def trova_permutazione_pythonic(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

print(trova_permutazione("dog", "godd"))
print(trova_permutazione_pythonic("dog", "god"))
    