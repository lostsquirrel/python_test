import re


def backward_string_by_word(text: str) -> str:
    # your code here
    p = re.compile(r"\w+")
    r = p.search(text)
    start = None
    result = ""
    while r is not None:
        if start is not None:
            result += ' ' * (r.start() - start)
        result += r.group(0)[::-1]
        start = r.end()
        r = p.search(text, start)
    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
