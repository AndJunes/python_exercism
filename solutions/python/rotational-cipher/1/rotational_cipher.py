"""Apply ROT-N cipher to a text."""
def rotate(text, key):
    result = []
    for char in text:
        if char.islower():
            posicion = ord(char) - ord('a')
            nueva = (posicion + key) % 26
            result.append(chr(nueva + ord('a')))
        elif char.isupper():
            posicion = ord(char) - ord('A')
            nueva = (posicion + key) % 26
            result.append(chr(nueva + ord('A')))
        else:
            result.append(char)
    return "".join(result)