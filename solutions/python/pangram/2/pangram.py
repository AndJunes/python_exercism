# Check if a sentence is a pangram (contains every letter of the alphabet at least once).
def is_pangram(sentence):
    """Determine if a sentence is a pangram.

    :param sentence: str - the input sentence to check.
    :return: bool - True if the sentence uses every letter of the English alphabet.
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(sentence.lower())