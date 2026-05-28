"""Determine if a word or phrase is an isogram."""
def is_isogram(string):
    """Make all letters lowercase and remove elements that can be repeated"""
    cleaned = string.lower().replace(" ", "").replace("-", "")
    return len(cleaned) == len(set(cleaned))