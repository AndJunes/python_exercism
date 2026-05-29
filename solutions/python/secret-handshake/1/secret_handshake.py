"""Secret handshake encoder."""

ACTIONS = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    """Convert a 5-character binary string to the secret handshake actions."""
    result = []
    for position, action in enumerate(ACTIONS):
        if binary_str[-(position + 1)] == "1":
            result.append(action)
    if binary_str[0] == "1":
        result.reverse()
    return result