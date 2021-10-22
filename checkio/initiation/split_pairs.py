def split_pairs(a):
    # your code here
    def is_even(n):
        return n % 2 == 0

    def chunk_string(string, length):
        return (string[i:length + i] for i in range(0, len(string), length))
    if not is_even(len(a)):
        a += "_"
    return chunk_string(a, 2)


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
