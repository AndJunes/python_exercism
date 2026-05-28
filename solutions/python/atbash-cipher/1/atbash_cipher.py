"""Atbash cipher: encode and decode using the ancient substitution scheme."""

ATBASH_TABLE = str.maketrans(
    'abcdefghijklmnopqrstuvwxyz',
    'zyxwvutsrqponmlkjihgfedcba'
)


def encode(plain_text):
    """Encode text with the Atbash cipher, grouping output in chunks of 5."""
    cleaned_characters = []
    for character in plain_text.lower():
        if character.isalnum():
            cleaned_characters.append(character)
    cleaned = ''.join(cleaned_characters)

    translated = cleaned.translate(ATBASH_TABLE)

    chunks = []
    for start in range(0, len(translated), 5):
        chunk = translated[start:start + 5]
        chunks.append(chunk)

    return ' '.join(chunks)


def decode(ciphered_text):
    """Decode an Atbash-ciphered text."""
    cleaned = ciphered_text.replace(' ', '')
    return cleaned.translate(ATBASH_TABLE)