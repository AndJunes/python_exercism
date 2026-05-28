"""Verify if an ISBN-10 is valid."""
def is_valid(isbn):
    "Verify length of 10, first 9 must be digits, last must be a digit or 'X', and calculate the formula"
    cleaned = isbn.replace("-", "")

    if len(cleaned) != 10:
        return False

    if not cleaned[:9].isdigit():
        return False

    if not (cleaned[9].isdigit() or cleaned[9] == "X"):
        return False

    total = 0
    for index, char in enumerate(cleaned):
        digit = 10 if char == "X" else int(char)
        total += digit * (10 - index)
    
    return total % 11 == 0