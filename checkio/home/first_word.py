def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    word_start = False
    word = ""
    word_parts = ("'", )
    for x in text:
        if x.isalpha() or x in word_parts:
            if not word_start:
                word_start = True
            word += x
        else:
            if word_start:
                return word
    return word


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    print(first_word("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")