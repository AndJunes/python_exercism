"""Bob will reply to someone when they say something to him or ask him a question."""

def response(hey_bob):

    text = hey_bob.strip()

    if text == "":
        return "Fine. Be that way!"

    is_question = text.endswith("?")
    is_yelling = text.isupper()

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_yelling:
        return "Whoa, chill out!"

    return "Whatever."