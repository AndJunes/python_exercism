"""Translate text from English to Pig Latin."""

def translate(text):
    """Convert English words into Pig Latin using defined rules."""

    vowels = "aeiou"
    words = text.split()
    translated_words = []

    for word in words:

        # Regla 1: vocal o casos especiales "xr" y "yt"
        if word[0] in vowels or word.startswith("xr") or word.startswith("yt"):
            translated_words.append(word + "ay")
            continue

        prefix_length = 0

        while prefix_length < len(word):

            # "qu" siempre se mueve como bloque
            if word[prefix_length:prefix_length + 2] == "qu":
                prefix_length += 2
                continue

            # 'y' se trata como consonante al inicio, pero como vocal después
            if word[prefix_length] == "y" and prefix_length != 0:
                break

            # consonantes iniciales
            if word[prefix_length] not in vowels:
                prefix_length += 1
            else:
                break

        translated_words.append(
            word[prefix_length:] + word[:prefix_length] + "ay"
        )

    return " ".join(translated_words)