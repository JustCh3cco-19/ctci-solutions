# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def caratteri_unici_pythonic(stringa):
    return len(set(stringa)) == len(stringa)

def caratteri_unici(stringa):
    # Assumiamo che il set di caratteri è ASCII (128 caratteri totali)
    if len(stringa) > 128:
        return False
    
    set_caratteri = [False] * 128
    for char in stringa:
        val = ord(char)
        if set_caratteri[val]:
            # Char già trovato quindi restituisco False
            return False
        set_caratteri[val] = True
    
    return True

print(caratteri_unici_pythonic("Ciao")) # True
print(caratteri_unici_pythonic("Hello")) # False perché c'è una l in più
print(caratteri_unici("Hello"))
print(caratteri_unici("Ciao"))