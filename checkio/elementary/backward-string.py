# -*- coding: utf-8 -*-
def backward_string(val: str) -> str:
    res = ""
    for x in val:
        res = x + res
        # print(res)
    # print(val.split())
    return res


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
