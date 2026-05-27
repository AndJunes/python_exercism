"verify that any and all pairs are matched and nested correctly."
def is_paired(input_string):
    "Any other characters should be ignored."
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    openings = "([{"
    for char in input_string:   
        if char in openings:
            stack.append(char)
        elif char in pairs:
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0