"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""

    prefix = vocab_words[0]

    result = [prefix]

    for word in vocab_words[1:]:
        result.append(prefix + word)

    return " :: ".join(result)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind."""

    base_word = word[:-4]

    if base_word.endswith("i"):
        return base_word[:-1] + "y"

    return base_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""

    words = sentence.split()

    return words[index].strip(".") + "en"

