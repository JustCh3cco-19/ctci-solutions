# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string, You can assume the string has only uppercase and lowercase letters (a-z).

def compress_string(stringa):
    compressed = []
    counter = 0

    for i in range(len(stringa)):
        if i != 0 and stringa[i] != stringa[i - 1]:
            compressed.append(stringa[i - 1] + str(counter))
            counter = 0
        counter += 1
    
    if counter:
        compressed.append(stringa[-1] + str(counter))

    return min(stringa, "".join(compressed), key=len)

print(compress_string("aabcccccaaa"))