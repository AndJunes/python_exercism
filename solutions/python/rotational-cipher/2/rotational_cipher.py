"""Apply ROT-N cipher to a text."""
def rotate(text, key):
    """Using a key of 0 or 26 will always yield the same output due to modular arithmetic."""
    result = []
    for char in text:
        if char.islower():
            position = ord(char) - ord('a')
            shifted = (position + key) % 26
            result.append(chr(shifted + ord('a')))
        elif char.isupper():
            position = ord(char) - ord('A')
            shifted = (position + key) % 26
            result.append(chr(shifted + ord('A')))
        else:
            result.append(char)
    return ''.join(result)