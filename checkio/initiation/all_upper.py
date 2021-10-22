def is_all_upper(text: str) -> bool:
    # your code here
    for x in text:
        if x != x.upper():
            print(x)
            return False

    return True


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER')
    assert not is_all_upper('all lower')
    assert not is_all_upper('mixed UPPER and lower')
    assert is_all_upper('')
    assert is_all_upper('     ')
    assert is_all_upper('444')
    assert is_all_upper('55 55 5')
    print("Coding complete? Click 'Check' to earn cool rewards!")
