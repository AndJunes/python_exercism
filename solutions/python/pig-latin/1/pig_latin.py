"""translate text from English to Pig Latin."""

def translate(text):
    """The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word"""
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:

        # Regla 1
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            result.append(word + "ay")
            continue

        i = 0

        while i < len(word):

            # Regla qu
            if word[i:i+2] == "qu":
                i += 2
                continue

            # Regla y (tratamiento especial)
            if word[i] == "y" and i != 0:
                break

            # consonantes normales
            if word[i] not in vowels:
                i += 1
            else:
                break

        result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)