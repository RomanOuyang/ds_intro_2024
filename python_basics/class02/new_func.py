def test(a,b):
    """
    test function for a+b
    """
    return a+b

if __name__ == '__main__':
    a = input('a')
    b = input('b')
    print(test(int(a), int(b)))
