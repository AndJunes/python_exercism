"""Find the anagrams of the word"""
def find_anagrams(word, candidates):
    """Find all candidates that are anagrams of the target word."""
    word_lower = word.lower()
    word_sorted = sorted(word_lower)

    anagrams = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if sorted(candidate_lower) == word_sorted and candidate_lower != word_lower:
            anagrams.append(candidate) 
    return anagrams